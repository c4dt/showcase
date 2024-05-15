# Updating the Showcase

This is a little todo-list of how to update the showcase

- create a new entry in the [updates/](./updates) directory

  - `big-update` if you go through all labs
  - `incremental-update` for small changes over multiple labs (commit updates)

- go through the list of labs and compare it with https://c4dt.epfl.ch/laboratory/

  - mark retired professors
  - add new labs

- for every lab, do

  - update the information in [data/labs.yaml]: url, description, contacts
  - if the contact person left the lab, delete it -> the `contact` entry will point to
    the professor
  - search for new projects
    - on the lab page
    - on github / source management
  - update the existing projects and test the links
    - update the last commit and the last update entry
    - click on all links (or use https://github.com/linkchecker/linkchecker)
    - make sure the papers point to https://infoscience.epfl.ch, with an additional link to
      arxiv if the infoscience page doesn't allow downloading the paper as a visitor

- create a PR and ask for comments

- once all labs are updated, for every lab, do

  - write an email to the professor
    - remind them the goals of the Factory and the Showcase
    - add a link to the projects of their lab
    - ask them if it's OK like that or if they want to add/remove/modify any entry
    - remind them that we do
      - maturity evaluation
      - promote projects
      - work on specific projects
    - CC one or two postdocs
    - remind them after a week or so

- think about adding some scripts, e.g.,
  - updating the github last commit and the `last_update`
  - going through all links and checking there is no 404
