## Purpose:
- GitHub Users can `read` a bunch of repositories owned by Organizations that they are not explicitly added to
- In the event this user is convered to an Outside Collaborator, the `read` access to these Internal repos can be lost. 
- This project helps you discover repos that a user can see but isn't given explicit access to, so that you can ensure these access privileges are updated

## Prerequisites:
1. Create a GitHub Actions secret with the PAT of the user who you want to audit

## About
This repository contains two python scripts:
1. get-repos-with-explicit-access.py - This script gets a list of repos that the user has explicit access to i.e. they were either invited specifically or added as a part of a GitHub Team
2. get-repos-without-explicit-access.py - This script outputs the list of repos that the user must be specifically added to

## Usage:
1. Run the manual workflow after you have ensured the Token is set properly

2. After successful execution, you will be able to download multiple reports:

  - `all-repos.csv`: This is the Master Set. It's a combination of every org-owned repository including internal and public the user is allowed to access

  - `explicit-access-repos.csv`: This is a subset of 2.1. It's a list of repos that the user is specifically allowed to access. It can be lesser than or equal to 2.1.

  - `to-be-added-manually.csv`: This is a Set Difference between 2.1 & 2.2 and is essentially the list of repos to which the user must be added to manually.
    
<img width="1182" alt="Screenshot 2022-04-04 at 11 25 13 PM" src="https://user-images.githubusercontent.com/48172220/161603134-f329f86f-3da5-4cc8-bc1a-286491bd0e71.png">

