#!/usr/bin/env python3.7
import time
import traceback
from datetime import datetime
from typing import List

import core
import prawcore
import pytz
from settings import settings
from utils import (
    calculate_stats,
    check_new_submissions,
    check_spam_submissions,
    handle_direct_messages,
    handle_modmail_messages,
    load_settings,
    look_for_rule_violations2,
    nsfw_checking,
    purge_old_records,
    send_broadcast_messages,
)

from moderatelyhelpfulbot.core import dbobj
from moderatelyhelpfulbot.models import reddit


def main_loop():
    s = dbobj.s  # noqa: E303 pylint: disable=invalid-name
    load_settings()

    sfw_subs = []
    nsfw_subs = []
    sfw_sub_list = "mod"
    nsfw_sub_list = "mod"

    i = 0
    while True:
        print("start_loop")
        try:
            i += 1
            UPDATE_LIST = core.UPDATE_LIST  # pylint: disable=invalid-name
            if UPDATE_LIST:
                print("updating list")
                # trs = s.query(TrackedSubreddit)
                # .filter(TrackedSubreddit.active_status != 0).all()
                trs = s.query(reddit.TrackedSubreddit).all()

                for tracked_subreddit in trs:
                    # print(tr.subreddit_name, tr.active_status)
                    assert isinstance(tracked_subreddit, reddit.TrackedSubreddit)

                    if tracked_subreddit.active_status > 0:
                        if tracked_subreddit.is_nsfw == 1:
                            nsfw_subs.append(tracked_subreddit.subreddit_name)
                        else:
                            sfw_subs.append(tracked_subreddit.subreddit_name)

                sfw_sub_list = "+".join(sfw_subs)
                nsfw_sub_list = "+".join(nsfw_subs)
                UPDATE_LIST = False  # pylint: disable=invalid-name
                s.commit()

            print(f"SFW sub list: {sfw_sub_list}")
            print(f"NSFW sub list: {nsfw_sub_list}")
            updated_subs: List[str] = []
            if nsfw_sub_list:
                updated_subs = check_new_submissions(sub_list=nsfw_sub_list)
                check_spam_submissions(sub_list=nsfw_sub_list)

            if sfw_sub_list:
                updated_subs += check_new_submissions(sub_list=sfw_sub_list)
                check_spam_submissions(sub_list=sfw_sub_list)

            start = datetime.now(pytz.utc)

            if i == 1:  # Don't skip any subs if first time runnign!
                updated_subs = None

            look_for_rule_violations2(
                do_cleanup=(i % 15 == 0), subs_to_update=updated_subs
            )  # uses a lot of resources

            if i % 75 == 0:
                purge_old_records()

            print(
                "$$$checking rule violations took this long",
                datetime.now(pytz.utc) - start,
            )

            # update_TMBR_submissions(look_back=timedelta(days=7))
            send_broadcast_messages()
            #  do_automated_replies()  This is currently disabled!!!!!!!!!!!!!!
            handle_direct_messages()
            handle_modmail_messages()

            nsfw_checking()
            if (i - 1) % 15 == 0:
                calculate_stats()

        except prawcore.exceptions.ServerError:
            time.sleep(60 * 5)  # sleep for a bit server errors
        except Exception:  # pylint: disable=broad-except
            trace = traceback.format_exc()
            print(trace)
            reddit.TrackedSubreddit.get_subreddit_by_name(
                settings["bot_name"]
            ).send_modmail(subject="[Notification] MHB Exception", body=trace)


if __name__ == "__main__":
    main_loop()
