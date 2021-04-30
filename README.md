# Codeforces-cli
## Python package
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
cf-cli [method name] [required parameter with value] [optional paramters with value]
`

## Example:

To get details of contest status.
`
cf-cli --contest-status --constestId 566 --handle Gellertke --from 1 --count 10
`
or
`
cf-cli --contest-status --cid 566 -h Gellertke -f 1 -c 10
`

## output

## Package required:<br>
- beautifulsoup4
- requests
- tabulate

Thanks for installing
