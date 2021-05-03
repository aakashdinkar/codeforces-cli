# Codeforces-cli
## Python package  [![pypi](https://pypi.org/static/images/logo-small.6eef541e.svg)](https://pypi.org/project/codeforces-cli/)
This package lets you show data for various methods in tabular format in your terminal.

### These following methods you can run:<br>
- blogEntry.comments
- blogEntry.view
- contest.hacks
- contest.list
- contest.ratingChanges
- contest.status
- problemset.problems
- problemset.recentStatus
- user.blogEntries
- user.info
- user.rating
- user.status

## How to install ?
`
pip install codeforces-cli
`

## How to use ?
`
python -m codeforces [method name] [required parameter with value] [optional paramters with value]
`

## Example:

To get details of contest status.

`

python -m codeforces --contest-status --constestId 566 --handle Gellertke --from 1 --count 10
`

or

`
python -m codeforces -cs -cid 566 -h Gellertke -f 1 -c 10
`

## Output
![image](https://user-images.githubusercontent.com/35952953/116748281-d720f680-aa1c-11eb-8ed4-eb6342394e3d.png)

## For help

`
python -m codeforces --help
`

or

`
python -m codeforces -h
`

![image](https://user-images.githubusercontent.com/35952953/116816381-4f9fc880-ab7f-11eb-84a8-609ca987f1d7.png)


## Package required:<br>
- beautifulsoup4
- requests
- tabulate

Thanks for Installing! 
