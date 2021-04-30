import hashlib
from request import codeforces_request
from tabulate import tabulate
from bs4 import BeautifulSoup
import datetime

class codeforces_method:
    def __init__(self):
        self.request = codeforces_request()
        self.help = "help"

    def show_help(self):
        print("""
        --blog-comment                  provide blogentryID for blogEntry.comments
        --blog-entry                    provide blogentryID for blogEntry.view
        --contest-hack                  provide contest id for contest.hacks
        --contest-list                  provide boolean value of gym for contest.list
        --contest-rating                provide contest id for contest.ratingChanges
        --contest-status                provide contest id for contest.status
        --problems                      provide tags for problemset.problems
        --problem-status                provide the number of count for problemset.recentStatus
        --user-blog                     provide user name for user.blogEntries
        --user-info                     provide user name for user.info
        --user-rating                   provide user name for user.rating
        --user-status                   provide user name for user.status
        """)

    def blog_comment(self, list_parameter):
        self.request.url += "blogEntry.comments"
        param = {
            "blogEntryId": list_parameter[0],
            "apikey": self.request.key,
            "time": self.request.time_now
        }
        str_ = f"{self.request.ran_num}/blogEntry.comments?apikey={param['apikey']}&blogEntryId={param['blogEntryId']}&time={param['time']}#{self.request.key}"
        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        data = []
        for item in json_data['result']:
            lst = []
            lst.append(item['id'])
            timestamp = datetime.datetime.fromtimestamp(item['creationTimeSeconds'])
            lst.append(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
            lst.append(item['commentatorHandle'])
            soup = BeautifulSoup(item['text'], 'html.parser')
            str_ = []
            ls = []
            for item in soup.find_all('div')[0].text.split():
                if "http" in item:
                    ls.append('\n')
                ls.append(item)
                if len(ls) == 7:
                    str_.append(" ".join(ls))
                    ls = [] 
            lst.append("\n".join(str_))
            data.append(lst)

        return tabulate(data, headers=["ID", "Date & Time", "Commentator Handle", "Comment"], tablefmt="grid")

    def blog_entry(self, list_parameter):
        self.request.url += "blogEntry.view"
        param = {
            "blogEntryId": list_parameter[0],
            "apikey": self.request.key,
            "time": self.request.time_now
        }
        str_ = f"{self.request.ran_num}/blogEntry.view?apikey={param['apikey']}&blogEntryId={param['blogEntryId']}&time={param['time']}#{self.request.key}"
        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        data = []
        lst = []
        lst.append(json_data['result']['id'])
        timestamp = datetime.datetime.fromtimestamp(json_data['result']['creationTimeSeconds'])
        lst.append(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
        lst.append(json_data['result']['authorHandle'])
        timestamp1 = datetime.datetime.fromtimestamp(json_data['result']['modificationTimeSeconds'])
        lst.append(timestamp1.strftime('%Y-%m-%d %H:%M:%S'))
        soup = BeautifulSoup(json_data['result']['title'], 'html.parser')
        lst.append(soup.find('p').text)
        lst.append(", ".join(json_data['result']['tags']))
        data.append(lst)

        return tabulate(data, headers=["ID", "Creation Time", "Author Handle","Modification Time", "Title", "Tags"], tablefmt="grid")

    
    def contest_hack(self, list_parameter):
        self.request.url += "contest.hacks"
        param = {
            "contestId": list_parameter[0],
            "apikey": self.request.key,
            "time": self.request.time_now
        }
        str_ = f"{self.request.ran_num}/contest.hacks?apikey={param['apikey']}&contestId={param['contestId']}&time={param['time']}#{self.request.key}"
        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        data = []
        for item in json_data['result']:
            lst = []
            lst.append(f"{item['problem']['contestId']}{item['problem']['index']}")
            timestamp = datetime.datetime.fromtimestamp(item['creationTimeSeconds'])
            lst.append(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
            lst.append(item['hacker']['members'][0]['handle'])
            lst.append(item['defender']['members'][0]['handle'])
            lst.append(item['problem']['name'])
            lst.append(", ".join(item['problem']['tags']))
            lst.append(item['judgeProtocol']['verdict'])
            data.append(lst)

        return tabulate(data, headers=["Contest ID", "Creation Time", "Hacker Handle", "Defender Handle", "Problem Name", "Tags", "Verdict"], tablefmt="grid")

    def contest_list(self, list_parameter):
        self.request.url += "contest.list"
        param = {
            "gym": list_parameter[0],
            "apikey": self.request.key,
            "time": self.request.time_now
        }
        str_ = f"{self.request.ran_num}/contest.list?apikey={param['apikey']}&gym={param['gym']}&time={param['time']}#{self.request.key}"
        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        data = []
        for item in json_data['result']:
            lst = []
            lst.append(item['id'])
            lst.append(item['name'])
            lst.append(item['type'])
            lst.append(item['phase'])
            lst.append(f"{item['durationSeconds']//60} mins")
        return tabulate(data, headers=["ID", "Name", "Type", "Phase", "Duration"], tablefmt="grid")

    def contest_rating(self, list_parameter):
        self.request.url += "contest.ratingChanges"
        param = {
            "contestId": list_parameter[0],
            "apikey": self.request.key,
            "time": self.request.time_now
        }
        str_ = f"{self.request.ran_num}/contest.ratingChanges?apikey={param['apikey']}&contestId={param['contestId']}&time={param['time']}#{self.request.key}"
        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        data = []
        for item in json_data['result']:
            lst = []
            lst.append(item['contestId'])
            lst.append(item['contestName'])
            lst.append(item['handle'])
            lst.append(item['rank'])
            lst.append(item['oldRating'])
            lst.append(item['newRating'])
            data.append(lst)
        
        return tabulate(data, headers=["contestID", "Contest Name", "Handle", "Rank", "Old Rating", "New Rating"], tablefmt="grid")


    def contest_status(self, list_parameter):
        self.request.url += "contest.status"
        param = {
            "contestId": list_parameter[0],
            "apikey": self.request.key,
            "time": self.request.time_now
        }
        str_ = f"{self.request.ran_num}/contest.status?apikey={param['apikey']}&contestId={param['contestId']}&time={param['time']}#{self.request.key}"
        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        data = []
        for item in json_data['result']:
            lst = []
            lst.append(item['id'])
            lst.append(item['problem']['name'])
            lst.append(item['problem']['tags'])
            lst.append(item['author']['members'][0]['handle'])
            lst.append(item['programmingLanguage'])
            lst.append(item['verdict'])
            lst.append(item['passedTestCount'])
            data.append(lst)
        
        return tabulate(data, headers=["ID", "Problem Name", "Tags", "Author Handle", "Programming Language", 'Verdict', 'Passed Testcases'], tablefmt="grid")

    def problems(self, list_parameter):
        self.request.url += "problemset.problems"
        param = {
            "tags": list_parameter[0],
            "apikey": self.request.key,
            "time": self.request.time_now
        }
        str_ = f"{self.request.ran_num}/problemset.problems?apikey={param['apikey']}&tags={param['tags']}&time={param['time']}#{self.request.key}"
        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        data = []
        for item, item2 in zip(json_data['result']['problems'],json_data['result']['problemStatistics']):
            lst = []
            lst.append(f"{item['contestId']}{item['index']}")
            lst.append(item['name'])
            lst.append(", ".join(item['tags']))
            lst.append(item['rating'])
            lst.append(item2['solvedCount'])
            data.append(lst)
        
        return tabulate(data, headers=["Problem ID", "Problem Name", "Problem Tags", "Problem Rating", "Solved Count"])

    def problems_status(self, list_parameter):
        self.request.url += "problemset.recentStatus"
        param = {
            "count": list_parameter[0],
            "apikey": self.request.key,
            "time": self.request.time_now
        }
        str_ = f"{self.request.ran_num}/problemset.recentStatus?apikey={param['apikey']}&count={param['count']}&time={param['time']}#{self.request.key}"
        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        data = []
        for item in json_data['result']:
            lst = []
            lst.append(item['id'])
            lst.append(f"{item['problem']['contestId']}{item['problem']['index']}")
            lst.append(item['problem']['name'])
            lst.append(", ".join(item['problem']['tags']))
            lst.append(item['author']['members'][0]['handle'])
            lst.append(item['programmingLanguage'])
            lst.append(item['verdict'])
            data.append(lst)
        
        return tabulate(data, headers=["ID", "Problem Id", "Problem Name", "Problem Tags", "Handle", "Language", "Verdict"])


    def user_blog(self, list_parameter):
        self.request.url += "user.blogEntries"
        param = {
            "handle": list_parameter[0],
            "apikey": self.request.key,
            "time": self.request.time_now
        }
        str_ = f"{self.request.ran_num}/user.blogEntries?apikey={param['apikey']}&handle={param['handle']}&time={param['time']}#{self.request.key}"
        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        data = []
        for item in json_data['result']:
            lst = []
            lst.append(item['id'])
            timestamp = datetime.datetime.fromtimestamp(item['creationTimeSeconds'])
            lst.append(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
            lst.append(item['authorHandle'])
            timestamp1 = datetime.datetime.fromtimestamp(item['modificationTimeSeconds'])
            lst.append(timestamp1.strftime('%Y-%m-%d %H:%M:%S'))
            if '<p' in item['title']:
                soup = BeautifulSoup(item['title'], 'html.parser')
                lst.append(soup.find('p').text)
            else:
                lst.append(item['title'])
            lst.append(", ".join(item['tags']))
            data.append(lst)

        return tabulate(data, headers=["ID", "Creation Time", "Author Handle","Modification Time", "Title", "Tags"], tablefmt="grid")


    def user_info(self, list_parameter):
        self.request.url += "user.info"
        param = {
            "handle": list_parameter[0],
            "apikey": self.request.key,
            "time": self.request.time_now
        }
        str_ = f"{self.request.ran_num}/user.info?apikey={param['apikey']}&handle={param['handle']}&time={param['time']}#{self.request.key}"
        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        data = []
        for item in json_data['result']:
            lst = []
            lst.append(item['lastName'])
            lst.append(item['firstName'])
            lastonline = datetime.datetime.fromtimestamp(item['lastOnlineTimeSeconds'])
            lst.append(lastonline.strftime('%Y-%m-%d %H:%M:%S'))
            lst.append(item['country'])
            lst.append(item['city'])
            lst.append(item['rating'])
            lst.append(item['friendOfCount'])
            lst.append(item['handle'])
            lst.append(item['organization'])
            Registered = datetime.datetime.fromtimestamp(item['registrationTimeSeconds'])
            lst.append(Registered.strftime('%Y-%m-%d %H:%M:%S'))
            lst.append(item['maxRank'])
            data.append(lst)

        return tabulate(data, headers=["Last Name", "First Name", "Last Online", "Country", "City", "Rating", 'Friends', 'Handle', 'Organization', 'Registered', 'Maximum Rank'], tablefmt="grid")


    def user_rating(self, list_parameter):
        self.request.url += "user.rating"
        param = {
            "handle": list_parameter[0],
            "apikey": self.request.key,
            "time": self.request.time_now
        }
        str_ = f"{self.request.ran_num}/user.rating?apikey={param['apikey']}&handle={param['handle']}&time={param['time']}#{self.request.key}"
        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        data = []
        for item in json_data['result']:
            lst = []
            lst.append(item['contestId'])
            lst.append(item['contestName'])
            lst.append(item['handle'])
            lst.append(item['rank'])
            lst.append(item['oldRating'])
            lst.append(item['newRating'])
            data.append(lst)
        
        return tabulate(data, headers=["Contest Id", "Contest Name", "Handle", "Rank", "Old Rating", "New Rating"], tablefmt="grid")

    def user_status(self, list_parameter):
        self.request.url += "user.status"
        param = {
            "handle": list_parameter[0],
            "apikey": self.request.key,
            "time": self.request.time_now
        }
        str_ = f"{self.request.ran_num}/user.blogEntries?apikey={param['apikey']}&handle={param['handle']}&time={param['time']}#{self.request.key}"
        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        data = []
        for item in json_data['result']:
            lst = []
            lst.append(item['id'])
            lst.append(item['problem']['name'])
            lst.append(item['problem']['tags'])
            lst.append(item['author']['members'][0]['handle'])
            lst.append(item['programmingLanguage'])
            lst.append(item['verdict'])
            lst.append(item['passedTestCount'])
            data.append(lst)
        
        return tabulate(data, headers=["ID", "Problem Name", "Tags", "Author Handle", "Programming Language", 'Verdict', 'Passed Testcases'], tablefmt="grid")