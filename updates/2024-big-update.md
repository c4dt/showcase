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

Know me: The C4DT Factory is in the process of updating the projects related
to digital trust from the affiliated labs at https://showcase.c4dt.org.

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
  - 03-05 - reply from Remi:
    - Pribot/Polisis/PoliCompare/Privyseal are projects from Hamza Harkous, a former Phd student.
      I actually met with him last week, those services are now supposed to be maintained by
      his partner at the University of Wisconsin.
      It looks like they are not doing their jobs :) Anyway, those services are quite old now.
      It is OK to remove them from your portofolio.
    - TinyGSN/ArgSM/Crowdsourcing Benchmark —> I don’t know about these projects.
      They are even older I guess. You can remove those.
    - Infoscience —> les papiers qui sont déjà en open-access ne sont généralement pas sur infoscience,
      is that bad?
    - media-observatory —> repo is public: https://github.com/mediaobservatory
    - For the active projects, we are maintaining the list here: https://modemos.epfl.ch/
  - 03-19 - answered to Rémi
- NAL - Katerina Argyraki
  - On lab page https://www.epfl.ch/labs/nal/
    - failing link to https://vigor.epfl.ch/ in `first framework for verifying software NFs with no verification expertise`
  - Added link in labs.yaml
  - Added github repo to labs.yaml
  - 2024-02-20 - sent email to Katerina - she replied with the following two projects
    - https://nal-epfl.github.io/WeHeY/
      - License
        - server - is it Apache, like the LICENSE.txt, or should it add the CRAPL-LICENSE.txt?
        - cli - no license
    - https://nal-epfl.github.io/tero-project/
      - no license
    - for both: rename the paper to something more specific
  - 2024-03-08 - answered Katerina's email with the suggestions from above
- ESL - David Atienza
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
  - sent email 2024-02-20
  - received reply that once they open source smth, OK
- DSLAB - George Candea
  - dslab.epfl.ch
    - link to ERC and intel are broken
  - sent email 2024-03-08
  - got answer 03-13
    - Here is a link to the version of PIX tailored specifically for eBPF code - https://github.com/dslab-epfl/ebpf-se.
      Please let me know if you have any questions/need additional information.
- LIONS - Volkan Cevher
  - lions.epfl.ch
  - Looked at webpage and saw a couple of other projects from 2019:
    - scopt, clash, alps, matrix-alps, tv-normed-pursuit, nys-sketch, LB-CSMRI
  - sent email 2024-03-08
- COMPSEC - Alessandro Chiesa
  - Added lab description
  - some old links on theory.epfl.ch
  - sent email 2024-03-08
  - received answer with project and website explanation

[//]: # " 10 "

- LSI - Giovanni De Micheli
  - Website
    - Not valid anymore:
      - Open Science Fund
      - the 2018 Xilinx Open Hardware University Design Competition 2018
  - Sent email on 2024-03-15
  - Answered 03-15
    - Hi,
      some of this work is obsolete, and should be deleted.
      The EPFL logic synthesis benchmarks are still available and maintained.
      Recent work addressed garbl;ed circuits (in the broad domain of crypto) and there are 3 pubs about it.
  - 2024-03-20 - Sent request for more information
- MMSPG - Touradj Ebrahimi
  - Website
    - https://grebproshare.epfl.ch/ - Links to app store not working
    - main site:
      - 404: Advanced image processing and analysis (http://moodle.epfl.ch/course/view.php?id=462)
      - 404: Bio-inspired processing of cognitive signals (http://moodle.epfl.ch/course/view.php?id=1851)
      - 404: EPFL-PoliMI Subjective Video Quality Assessment Database (http://vqa.como.polimi.it/index.htm)
        - working link: https://vqa.como.polimi.it
      - 404: Information Processing for Video Surveillance (http://spie.org/x1139.xml?course_id=E0838267&search_text=ebrahimi&format=All)
      - 404: All links on the right side of https://www.epfl.ch/labs/mmspg/research/page-58317-en-html/
      - 404: All links on the right side of https://www.epfl.ch/labs/mmspg/research/page-58342-en-html/
      - 404: Most links on the right side of https://www.epfl.ch/labs/mmspg/research/page-58351-en-html/
      - 404: Link on the right side of https://www.epfl.ch/labs/mmspg/research/page-58363-en-html/
      - 404: Lutz Goldmann, Lin Yuan, Anne-Flore Perrin, Irene Viola on https://www.epfl.ch/labs/mmspg/mmspg-alumni/
      - 404/Certificate error: MPEG and DMP on https://www.epfl.ch/labs/mmspg/innovation/
      - Download error: when trying to use the ftp connection from https://www.epfl.ch/labs/mmspg/downloads/mj-pccd/
      - 404: Link on the right side of https://www.epfl.ch/labs/mmspg/meetings/
  - Sent email on 2024-03-15
- PARSA - Babak Falsafi
  - Website OK
  - Sent email on 2024-03-15
- LIA - Boi Faltings
  - Website
    - Location - How to reach the LIA using public transport - Zürich Airport
  - Sent email on 2024-03-20
- DEDIS - Bryan Ford
  - Website
    - Link to list of projects https://github.com/dedis/doc is archived
    - "our blog" is from 2020
    - 404 - "page at stack overflow"
  - updated last commits
  - changed github URL for dela and d-voting to c4dt/
  - Sent email on 2024-03-21
- LTS4 - Pascal Frossard
  - Removed Seyed from lab description
  - Sent email on 2024-03-21
  - Included suggestions from sahar.sadrizadeh@epfl.ch from 2024-04-08 on 2024-04-12
- INDY - Matthias Grossglauser
  - Website indy.epfl.ch:
    - 413 - URL `../assets/img/apple-icon.png'
    - ConnectionTimeout `http://icapeople.epfl.ch/grossglauser/' - `Matthias Grossglauser'
  - Removed contacts from projects
  - Sent email on 2024-03-21
- DCL - Rachid Guerraoui
  - Website
    - some internal CORS and scripts not found error
    - Failing links to people who left: matej.pavlovic, dragos-adrian.seredinschi, matteo.monti, athanasios.xygkis
  - Projects
    - talk and zebra on github.com/Distributed-EPFL
    - public version of chop-chop?
    - missing READMEs and LICENSEs...
  - Github organizations
    - https://github.com/Distributed-EPFL and https://github.com/LPD-EPFL ?
  - Sent email on 2024-03-22
- LAP - Paolo Ienne
  - Website dynamatic.epfl.ch has wrong link to https://dynamatic.epfl.ch/images/EPFL%20marks%2050%20years%20of%20scientific%20progress.mp4
  - Sent email on 2024-03-22
- MLO - Martin Jaggi
  - updated last commits
  - update contacts
  - existing projects
    - disco: https://epfml.github.io/disco/#/list - says disco server is not running
  - lab page:
    - Empty or broken links:
      - `AISTATS Paper on Adaptive First-Order Optimization`
      - `AISTATS results on Frank-Wolfe, and Optimal Transport`
      - https://thijsvogels.nl
      - Links to AMLD workshops:
        - `NLP track`: `https://appliedmldays.org/tracks`
        - `Theory meets Practice Workshop`: `https://appliedmldays.org/workshops/advances-in-ml-theory-meets-practice`
        - `PyTorch Workshop`: `https://appliedmldays.org/workshops/pytorch-tutorial`
        - `Industry Track`: `https://www.appliedmldays.org/2019/tracks/6`
        - `the first instance of the Applied ML Days`: `https://www.appliedmldays.org/2017`
      - other links:
        - `Electric Vehicle Charging`: `https://www.faculty.ece.vt.edu/kekatos/papers/CDC2016.pdf`
        - `Summer school`: `https://www.ds3-datascience-polytechnique.fr/day-4-5-sessions/`
        - `Machine Learning Course Started`: `https://mlo.epfl.ch/page-146520.html`
        - `Google Focused Research Award`: `https://ai.google/research/outreach/focused-research-awards/`
        - `Greedy and Coordinate Algorithms at AISTATS`: `http://www.aistats.org/accepted.html`
        - `Welcome Mikhail and Sebastian`: `/mlo/page-135382-en-html/`
        - `Machine Learning Course Started`: `mlo.epfl.ch/page-136795.html`
        - `news article`: `https://www.inf.ethz.ch/news-and-events/spotlights/semeval2016.html`
        - `here`: `http://www.jmlr.org/proceedings/papers/v37/mab15.html`
        - `Algorithms in the wild`: `https://blogs.nvidia.com/blog/2018/03/20/big-blue-touts-partnership-with-nvidia-at-ibm-think-confab/`
        - `SDSC fellowship`: `https://datascience.ch/academic-projects/`
        - `Paper “Primal-Dual Rates and Certificates” at ICML`: `http://jmlr.org/proceedings/papers/v48/dunner16.html`
    - new projects
      - Meditron
      - Megatron
      - Also various new github repos - which ones are worth to be shown?
  - Sent email on 2024-04-12

[//]: # " 20 "

- RS3LAB - Sanidhya Kashyap
- SACS - Anne-Marie Kermarrec
- LARA - Viktor Kunčak
- SFI-SM - Semyon Malamud
- LAMP - Martin Odersky
- DESL-PWRS - Mario Paolone
- HexHive - Mathias Payer
- Clément Pit-Claudel
- SalatheLab - Marcel Salathé
- Yanina Shkel

[//]: # " 30 "

- IVRL - Sabine Süsstrunk
- SPRING - Carmela Troncoso
- LASEC - Serge Vaudenay
- DLAB - Robert West

[//]: # " Labs w/o code "

- SFI-PCD - Pierre Collin-Dufresne
- SFI-RF - Ruediger Fahlenbrach
- SFI-JH - Julien Hugonnier
- LDS - Jean-Pierre Hubaux
  - retired
- LCA2 - Jean-Yves Le Boudec
  - retired
- GR-FE - Jacques Fellay
- SFI - Damir Filipovic
- VLSC - James Larus
  - retired
