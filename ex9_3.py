import requests
import sys


def rank_ques(n, label):
    url = 'https://api.stackexchange.com/2.2/questions'
    param = {
        'pagesize': n,
        'order': 'desc',
        'sort': 'votes',
        'tagged': label,
        'site': 'stackoverflow'
    }
    r = requests.get(url, params=param)
    data = r.json()['items']
    for ques in data:
        answer_id = ques.get('accepted_answer_id')
        if answer_id is None:
            print("title is : {} and this question no answer accept".format(
                ques.get("title")))
        else:
            print("title is : {}".format(ques.get('title')))
            print("answer is:http://stackoverflow.com/a/{}".format(answer_id))


def main():
    n = sys.argv[1]
    label = sys.argv[2]
    rank_ques(n, label)


if __name__ == "__main__":
    main()
