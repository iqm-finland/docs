# IQM SDK & Docs

This repository holds the mirror of the source code of IQM SDK — a collection of libraries for operating IQM's quantum computers.
It also builds and publishes documentation pages for those libraries: [https://docs.meetiqm.com/](https://docs.meetiqm.com/).
The versions in this mirror correspond to the latest stable release of IQM QCCSW (Quantum Computing Control Software).

This GitHub repository is a read-only mirror that isn't used for accepting contributions.

# Building the documentation locally
It uses a Python script in `generate_search_index.py` to generate a search index for the documentation. To build the documentation locally, you need to have Python installed and then run the script based on the folders, or retrieve a `search.json` document from the GitHub repository and the [GitHub Pages branch](https://github.com/iqm-finland/docs/tree/gh-pages).

In order to locally run the React application, you need to have Node.js installed. Then you can run the following commands:

```bash
npm install
npm run dev
```

or use Yarn:
```bash
yarn install
yarn  dev
```

