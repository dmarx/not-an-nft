# not-an-nft

git is the only blockchain that matters.

lol fork me and add conflicting commits if you're feeling sassy!

## components

1. gh-pages image hosting site. start with jupyterbook or something simple.
  - event0: takes an image folder and returns a markdown file with the images embedded
  - event1: runs event0 and updates a jupyterbook _toc
    - more generally: publish to PyPI a small utility that automagically updates toc from folder path structure
2. commit PGP keys with images
  - event2: called by event0, assigns PGP key pair for each unassigned image in folder
  - event3: automates commit and push, triggers gh workflow that buils and publishes site
3. add private key filetype to .gitignore. add comment explaining what this is for


maybe we could invert this? the purchaser is paying to have their key added... oh right: [shitty permissions](https://github.com/dmarx/bench-warmers/blob/main/free-to-mint-nfts_git_plus_pgp.md).


to do:
- learn more about PGP keys and modern crypto
