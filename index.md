<!-- ## Welcome to Tracer's Site  -->

<!-- You can use the [editor on GitHub](https://github.com/TracerTool/TracerTool.github.io/edit/main/index.md) to maintain and preview the content for your website in Markdown files. -->

<!-- Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files. -->

## Tracer: Finding Patches for Open Source Software Vulnerabilities
The paper has been submitted to ICSE 2022.

This page lists the supplementary materiales that are omitted from the paper due to space limitations, provides ... of our study RQ..., and releases the data and code for the tool.

### Table of Contents
* [Tracer](#Tracer)
* [Empirical Study](#Empirical-Study)
* [Tracer Code](#Tracer-Code)
* [Evaluation](#Evaluation)


### Tracer
Open source software (OSS) vulnerability management has been becoming an open problem. Vulnerability databases provide valuable data that are needed to address open source vulnerabilities. Recently, there arises a growing concern about the information quality of vulnerability databases. In particular, it is unclear how is the quality of vulnerability patches in vulnerability databases, and the existing manual or heuristic-based approaches for patch identification are either too expensive or too specific to be applied to all open source vulnerabilities.

To address these problems, we first conduct an empirical study to understand the quality and characteristics of patches for OSS vulnerabilities in two state-of-the-art vulnerability databases, i.e., Veracode's and Snyk's databases. Our study is designed to cover five dimensions, i.e., patch coverage, patch consistency, patch type, mapping cardinality between vulnerabilities and their patches, and patch accuracy. Then, inspired by our study, we propose the first automated approach, named **Tracer**, to **find patches for an OSS vulnerability from multiple sources**. Our key idea is that patch links will be frequently referenced during the reporting, discussion, and resolution of an OSS vulnerability.

Our extensive experiments indicated that Tracer could find patches for up to 273.8% more CVEs than existing heuristic-based approaches while having a significantly higher F1-score by up to 116.8%. Compared to state-of-the-art vulnerability databases, Tracer could achieve a 15.5% to 18.4% higher recall, but sacrifice up to 12.0% CVEs' patches and 6.3% lower precision. Our evaluation also demonstrated the generality and the usefulness of Tracer in practice with a user study.

### Empirical Study

**Breadth Dataset:**  We built a breadth dataset of OSS vulnerabilities by acquiring all open source vulnerabilities from $DB_A$​ and $DB_B$​ as of April 7, 2020. We obtained 8,630 and 5,858 CVEs from $DB_A$​ and $DB_B$​​ respectively. The data can be found [here](https://github.com/TracerTool/TracerTool.github.io/tree/main/Experimental%20Data/Empirical%20Study). 

**Depth Dataset:**  For each CVE, two of the authors separately found its patches by analyzing patches reported by the three databases, looking into CVE description and references in NVD, and searching GitHub repositories and Internet resources. Then, they exchanged sources and ways to find patches. After that, another authors participated in. They investigated inconsistent cases together, and revisited all CVEs for several rounds until reaching a consensus. Finally, they successfully found patches for 1,295 CVEs. 

We release the dataset [here](https://github.com/TracerTool/TracerTool.github.io/blob/main/Experimental%20Data/Empirical%20Study/depth_dataset.csv). And We hope it can be a basis for possible follow-up research, which requires accurate mapping between CVEs and patches. Although we have tried best to ensure its accuracy, mistakes still be possible. If you find anything wrong, please kindly report an issue. So many thanks for your effort!  Let's maintain it together 😄. 

### Tracer Code

You can download source code from [here (toadd)]( .. ).

### Evaluation

**Generality Evaluation:** To evaluate the generality of Tracer to a wider range of OSS vulnerabilities, We construct two more datasets [here](https://github.com/TracerTool/TracerTool.github.io/tree/main/Experimental%20Data/Evaluation/Generality%20Evaluation%20datasets). 

**Usefulness Evaluation (User Study):** To evaluate the usefulness of Tracer in practice, we conducted a user study with 10 participants to find patches of 10 CVEs. The 10 tasks can be found [here](https://github.com/TracerTool/TracerTool.github.io/tree/main/Experimental%20Data/Evaluation/Usefulness%20Evaluation%20tasks). 





<!-- ### Jekyll Themes   -->

<!-- Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/TracerTool/TracerTool.github.io/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.   -->

<!-- ### Support or Contact   -->

<!-- Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.   -->
