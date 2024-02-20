Showcase modifications in 2024-02

- General feedback

  - webpages of the labs projects should have dates
    - creation date
    - updates

- yaml for new projects

```yaml
projects:
  url_path:
    name: (lowercase short name with spaces)
    description: >
      (Short description, will be shown under the name)
    tech_desc: >
      (A more detailed description in 2-3 sentences for somebody knowledgeable in the subject)
    layman_desc: >
      (A 2-3 sentence description for somebody with general knowledge)
    type: ( Application | Library | Framework | Toolset | Simulation | Experiments )
    categories:
      - ( Privacy | Blockchain | Verification | Security | Learning | Other )
    applications:
      - ( Finance | Health | Gov | Infra | Info | Other )
    tags:
      - (Add tags, if possible out of the existing ones)
    url: (URL for a home page)
    code:
      type: (Lab Github, Personal Gihub, zip files, ...)
      url: (https://...)
      date_last_commit: (YYYY-MM-DD)
    doc: (url to documentation)
    lines_of_code: (# of codelines)
    language: (What the majority of the code is written in)
    license: (BSD, GPL 3+, MPL 2+, Apache, ...)
    date_added: (YYYY-MM-DD)
```

- email for professors:

```
Hi ,

Might not know me: I’m Linus from the C4DT Factory - we’re working on the
projects from the labs to learn the latest tech and link it to our partners.
About once per year we update our list of projects at https://showcase.c4dt.org.

Know me: The C4DT Factory is in the process of updating the projects from the
affiliated labs at https://showcase.c4dt.org.

We concentrate on the projects with a software component that is actively worked
on and related to digital trust.
Currently we have the following list of projects related to digital trust
from your lab:

https://factory.c4dt.org/showcase/#dropdown=lab_FILLIN

Do you think we’re missing any important work related to digital trust from your lab,
and which has an associated, publicly available software artefact?

Projects w/o code: I found the following two projects which look very interesting,
and would like to know if there is software available, as I couldn’t find it on the website:

No projects: Currently we have no projects listed from your lab. If you think there are one or more projects with software artefacts, could you point me to them so I can add them to the list?

I also ran a link checker on your lab site and found the following failing links:

Happy to answer any questions you might have,

Linus
```

- LSIR - Karl Aberer
  - update lab url
  - pribot:
    - dead link from https://www.epfl.ch/labs/lsir/pribot/ to https://pribot.org/bot
  - ai-data-platform-v1
    - dead link from https://www.epfl.ch/labs/lsir/ai-research-aiding-online-children-safety/ to https://modemos.epfl.ch/main
    - removed demo from project entry
  - ai-data-platform-v2
    - not in infoscience
  - scilens
    - broken link in https://scilens.epfl.ch -> `Details` -> `System` -> `NewsTeller`
  - media-observatory:
    - removed contact 'Jérémie Rappaz'
    - github repo is private - is that Jérémie's? Or somebody else's?
  - website
    - dead links on "Go try it now" on Polisis and others: https://www.epfl.ch/labs/lsir/polisis/
      - Polisis
      - PoliCompare
      - Pribot
      - Privyseal
      - TinyGSN - "You don't have access"
      - ArgSM - "You don't have access"
      - Crowdsourcing Benchmark - "You don't have access"
  - Added github repo to labs.yaml
  - 2024-02-20 - sent email to Remi
- NAL - Katerina Argyraki
  - On lab page https://www.epfl.ch/labs/nal/
    - failing link to https://vigor.epfl.ch/ in `first framework for verifying software NFs with no verification expertise`
  - Added link in labs.yaml
  - Added github repo to labs.yaml
  - 2024-02-20 - sent email to Katerina
- ## ESL - David Atienza
  - Added github repo to labs.yaml
  - removed homepage for gem5-x project
  - modified link for gem5-x project
  - modified link for 3d-ice project
  - lab website
    - in the top bar, the `IEM` doesn't have a valid URL: https://sti.epfl.ch/fr/recherche/instituts/iem/
    - https://www.epfl.ch/labs/esl/research/personalized-health/ misses "Epilepsy monitoring" in the main text
    - https://www.epfl.ch/labs/esl/research/open-source-tools-datasets/ has many 404 links
  - Added projects:
    - hdtorch
    - cloud-performance-monitor
    - digital-twins
  - 2024-02-20 - sent email to David
  - David replied, asking to add
    - https://www.epfl.ch/labs/esl/research/systems-on-chip/x-heep/
- Antoine Bosselut
  - added lab to list
  - doesn't seem to have a lab github
  - Added projects:
    - PeaCoK - no license
    - Disco
    - Meditron
    - CroW - no license
  - nlp.epfl.ch links:
    - https://nlp.epfl.ch/publications.html: Comfact "Dataset" link is broken
  - https://factory.c4dt.org/showcase/#dropdown=lab_NLP
  - 2024-02-20 - sent email to Antoine
- Thomas Bourgeat
  - no lab page yet
- DCSL - Edouard Bugnion
- DSLAB - George Candea
- LIONS - Volkan Cevher
- COMPSEC - Alessandro Chiesa
- SFI-PCD - Pierre Collin-Dufresne
- LSI - Giovanni De Micheli
- MMSPG - Touradj Ebrahimi
- SFI-RF - Ruediger Fahlenbrach
- PARSA - Babak Falsafi
- LIA - Boi Faltings
- GR-FE - Jacques Fellay
- SFI - Damir Filipovic
- DEDIS - Bryan Ford
- LTS4 - Pascal Frossard
- INDY - Matthias Grossglauser
- DCL - Rachid Guerraoui
- LDS - Jean-Pierre Hubaux
  - retired
- SFI-JH - Julien Hugonnier
- LAP - Paolo Ienne
- MLO - Martin Jaggi
- RS3LAB - Sanidhya Kashyap
- SACS - Anne-Marie Kermarrec
- LARA - Viktor Kunčak
- VLSC - James Larus
- LCA2 - Jean-Yves Le Boudec
  - retired
- SFI-SM - Semyon Malamud
- LAMP - Martin Odersky
- DESL-PWRS - Mario Paolone
- HexHive - Mathias Payer
- Clément Pit-Claudel
- SalatheLab - Marcel Salathé
- Yanina Shkel
- IVRL - Sabine Süsstrunk
- SPRING - Carmela Troncoso
- LASEC - Serge Vaudenay
- DLAB - Robert West
