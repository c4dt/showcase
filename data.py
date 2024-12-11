#!/usr/bin/env python3

import codecs
import os

from functools import lru_cache

import strictyaml as sy

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(ROOT_PATH, 'data')
LABS_FILENAME = 'labs.yaml'
PROJECTS_FILENAME = 'projects.yaml'

LABS_SCHEMA = sy.Map({"labs":
    sy.MapPattern(sy.Str(),
        sy.Map({
            "name": sy.Str(),
            "prof": sy.Map({
                "name": sy.Seq(sy.Str()),
                "email": sy.Email(),
                }),
            "description": sy.Str(),
            "url": sy.Url(),
            sy.Optional("contacts"): sy.Seq(
                sy.Map({
                    "name": sy.Str(),
                    sy.Optional("email"): sy.Email(),
                    }),
                ),
            sy.Optional("notes"): sy.Str(),
            sy.Optional("information"): sy.Seq(
                sy.Map({
                    "title": sy.Str(),
                    "url": sy.Url(),
                    sy.Optional("notes"): sy.Seq(
                        sy.Map({
                            sy.Optional("label"): sy.Str(),
                            "text": sy.Str(),
                            sy.Optional("url"): sy.Url(),
                        }),
                    ),
                }),
            ),
        }),
        )
    })

PROJECTS_SCHEMA = sy.Map({"projects":
    sy.MapPattern(sy.Str(),
        sy.Map({
            "name": sy.Str(),
            "description": sy.Str(),
            "type": sy.CommaSeparated(sy.Enum([
                "Application",  # Stand-alone code with useful functionality outside of the paper
                "Library",      # Code to be included in other projects outside of the paper
                "Framework",    # A set of concepts and best practices for a given task
                "Toolset",      # Various stand-alone applications for a given task
                "Simulation",   # Generic code that can be used to run simulations described in the paper
                "Experiments",  # Code that produces figures and graphs of the paper
                "Hands-on",     # Stand-alone hands-on workshop
            ])),
            "categories": sy.Seq(sy.Enum([
               "Privacy",
               "Blockchain",
               "Verification",
               "Security",
               "Learning",
               "Other"
            ])),
            "applications": sy.Seq(sy.Enum([
                "Finance",
                "Health",
                "Gov",
                "Infra",
                "Info",
                "Other"
            ])),
            "tags": sy.Seq(sy.Enum([
                "Access Control", "Adversarial", "Anonymity", "Attack",
                "Benchmark", "Binary", "Bluetooth", "Byzantine Resilience",
                "Cloud", "Code Analysis", "Computer Vision", "Concurrency", "Consensus", "CrowdSource",
                "Data Structures", "Database", "Debug", "Decentralized", "Deep Neural Networks",
                "Development", "Distributed Learning",
                "Encryption", "Exploit",
                "Failure", "Features", "Federated Learning", "Fuzzing",
                "Homomorphic Encryption",
                "Image Classification", "Images", "Inductive Bias", "Internet of Things",
                "Locking", "Low-Level",
                "Machine Learning", "Mobile App",
                "Natural Language", "Network",
                "Optimization",
                "Predictor", "Protection", "Protocol", "PyTorch",
                "Secure Multi-Party Computation", "Server", "Simulator", "Static Analysis", "Survey",
                "TensorFlow", "Tor",
                "Zero-Knowledge Proofs"
            ])),
            "date_added": sy.Datetime(),

            sy.Optional("layman_desc"): sy.Str(),
            sy.Optional("tech_desc"): sy.Str(),
            sy.Optional("notes"): sy.Str(),
            sy.Optional("url"): sy.Url(),
            sy.Optional("contacts"): sy.Seq(
                sy.Map({
                    "name": sy.Str(),
                    sy.Optional("email"): sy.Email(),
                    sy.Optional("url"): sy.Url(),
                }),
            ),
            sy.Optional("code"): sy.Map({
                "type": sy.Str(),
                sy.Optional("url"): sy.Url(),
                sy.Optional("date_last_commit"): sy.Datetime(),
                }),
            sy.Optional("doc"): sy.Url(),
            sy.Optional("lines_of_code"): sy.Str(),
            sy.Optional(
                "c4dt_contact",
                default={"name": "C4DT team", "email": "c4dt-dev@listes.epfl.ch"}
            ): sy.Map({
                "name": sy.Str(),
                "email": sy.Email(),
                }),
            sy.Optional("language"): sy.Str(),
            sy.Optional("license"): sy.CommaSeparated(sy.Enum([
                "AGPL-3.0",
                "GPL-2.0", "GPL-3.0",
                "GPL-2.0+", "GPL-3.0+",
                "LGPL-3.0",
                "MPL-2.0", "MPL-2.0+",
                "MIT",
                "Apache-2.0",
                "BSD-2-Clause",
                "BSD-3-Clause",
                "BSD-3-Clause Clear",
                "CeCILL-B",
                "CloudSuite",
                "CC BY 4.0",
                "SOLDERPAD HARDWARE LICENSE",
                "commercial",
                "non-commercial",
                "other",
                "various"
                ])),
            sy.Optional("information"): sy.Seq(
                sy.Map({
                    "type": sy.Str(),
                    "url": sy.Url(),
                    "title": sy.Str(),
                    sy.Optional("notes"): sy.Seq(
                        sy.Map({
                            sy.Optional("label"): sy.Str(),
                            "text": sy.Str(),
                            sy.Optional("url"): sy.Url(),
                            }),
                        ),
                    }),
                ),
            sy.Optional("maturity"): sy.Int(),
            sy.Optional("incubator"): sy.Map({
                "work": sy.Str(),
                sy.Optional("type", default="incubated"): sy.Enum([
                    "incubated",
                    "incubated_market",
                    "retired",
                    "retired_archived",
                    ]),
                sy.Optional("products"): sy.Seq(
                    sy.Map({
                        "type": sy.Enum(["Demo", "Demo-Code", "hands-on", "Pilot", "App", "Library", "OSS-participation", "Archive", "Blog"]),
                        "url": sy.Url(),
                        "title": sy.Str(),
                        }),
                    )
                }),
            sy.Optional("date_updated"): sy.Datetime()
            | sy.EmptyList(),
            }),
        )
    })


@lru_cache(maxsize=1)
def load():
    with codecs.open(os.path.join(DATA_PATH, LABS_FILENAME),
            encoding='utf-8') as f:
        labs_yaml = sy.load(f.read(), LABS_SCHEMA, label=f.name)
        labs = labs_yaml['labs'].data

    for lab_id, lab in labs.items():
        project_file = os.path.join(DATA_PATH, lab_id, PROJECTS_FILENAME)
        if not os.path.exists(project_file):
            continue
        with codecs.open(project_file,
                encoding='utf-8') as f:
            projects_yaml = sy.load(f.read(), PROJECTS_SCHEMA, label=f.name)
        lab['projects'] = projects_yaml['projects'].data

    return labs

if __name__ == '__main__':
    import sys, os
    data = load()
    if len(sys.argv) != 2:
        print("\n".join(data.keys()))
        sys.exit(0)

    if sys.argv[1] in data:
        print("\n".join(data[sys.argv[1]]['projects'].keys()))
