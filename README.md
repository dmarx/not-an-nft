# not-an-nft

git is the only blockchain that matters.

lol fork me and add conflicting commits if you're feeling sassy!

## components

1. gh-pages image hosting site. start with jupyterbook or something simple.
2. commit PGP keys with images
3. save private keys mirrored to folder in .gitignore. or rather, the canonical folder is in gitignore, 
   and there's a designated location for copying stuff to be committed and shared publicly
4. build a utility that facilitates this process:
  - takes an image folder as input
  - for each image, 
    - generates a PGP pair
    - copies artifacts to publication folder
    - commits the new images files
    - pushes to github
  - ...duh, even more simply: just add the private key filetype to .gitignore. no copying needed. just generate a key and commit.
  
on that note: time to learn how to generate a pgp keypair

maybe we could invert this? the purchaser is paying to have their key added... oh right: [shitty permissions](https://github.com/dmarx/bench-warmers/blob/main/free-to-mint-nfts_git_plus_pgp.md).
