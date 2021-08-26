## Welcome to PatFinder's Site 

<!-- You can use the [editor on GitHub](https://github.com/PatFinderTool/PatFinderTool.github.io/edit/main/index.md) to maintain and preview the content for your website in Markdown files. -->

<!-- Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files. -->

### PatFidner: Finding Patches for Open Source Software Vulnerabilities

Open source software (OSS) vulnerability management has been becoming an open~problem. Vulnerability databases provide valuable data that are needed~to address open source vulnerabilities. Recently, there arises a growing concern about the information quality of vulnerability databases.~In particular, it is unclear~how~is the quality of vulnerability patches~in vulnerability databases, and the existing manual or heuristic-based~approaches for patch identification are either too expensive~or~too~specific to be applied to all open source vulnerabilities.

To address these problems, we first conduct~an empirical~study~to understand the quality and characteristics~of~patches for OSS vulnerabilities in two state-of-the-art vulnerability databasescongyingEdit{, i.e., Veracode's and Snyk's databases. Our study is designed to cover five dimensions, i.e., patch coverage,~patch consistency, patch type, mapping cardinality between~vulnerabilities and their patches, and patch accuracy. Then, inspired~by~our~study, we propose the first automated approach, named PatFidner,~to~find patches for an OSS vulnerability from multiple sources. Our key idea is that patch links will be frequently referenced during the reporting, discussion, and resolution of an OSS vulnerability.

Our extensive experiments indicated that ParFinder could find patches for up to 273.8% more CVEs than existing heuristic-based~approaches while having a significantly~higher F1-score by~up to 116.8%. Compared to state-of-the-art vulnerability databases, ParFinder could achieve a 15.5% to 18.4% higher~recall, but sacrifice~up~to 12.0% CVEs' patches and 6.3% lower precision. Our evaluation~also~demonstrated the generality and the usefulness of PatFidner in practice with a user study.


### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/PatFinderTool/PatFinderTool.github.io/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
