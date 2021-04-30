from methods import codeforces_method
import sys

def codeforces():
    code_method = codeforces_method()
    list_parameter = [sys.argv[-1]]
    switcher = {
        "--blog-comment": code_method.blog_comment,
        "--blog-entry": code_method.blog_entry,
        "--contest-hack": code_method.contest_hack,
        "--contest-list": code_method.contest_list,
        "--contest-rating": code_method.contest_rating,
        "--contest-status": code_method.contest_status,
        "--problems": code_method.problems,
        "--problem-status": code_method.problems_status,
        "--user-blog": code_method.user_blog,
        "--user-info": code_method.user_info,
        "--user-rating": code_method.user_rating,
        "--user-status": code_method.user_status
    }
    if len(sys.argv) < 3 and sys.argv[-1] == '--help':
        code_method.show_help()
    elif sys.argv[-2] in switcher:
        print(switcher[sys.argv[-2]](list_parameter))

if __name__ == '__main__':
    codeforces()