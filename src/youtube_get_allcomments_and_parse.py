from v1.service.Comment.comments_helper import build_initial_request, parse_result

all_comments=list()

def main():
    # Build request and fetch comments
    request = build_initial_request("_0JZbsJdFIU")
    result= request.execute()
    parse_result(result, all_comments)

    print(all_comments)
    print(len(all_comments))

main()
