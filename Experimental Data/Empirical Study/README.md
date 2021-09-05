##### Breadth Dataset

We built a breadth dataset of OSS vulnerabilities by acquiring all open source vulnerabilities from $DB_A$​ and $DB_B$​ as of April 7, 2020. We obtained 8,630 and 5,858 CVEs from $DB_A$​ and $DB_B$​​ respectively. 

#####  Depth Dataset

For each CVE, two of the authors separately found its patches by analyzing patches reported by the three databases, looking into CVE description and references in NVD, and searching GitHub repositories and Internet resources. Then, they exchanged sources and ways to find patches. After that, another author participated in. They investigated inconsistent cases together, and revisited all CVEs for several rounds until reaching a consensus. Finally, they successfully found patches for 1,295 CVEs. 

---

##### Update

We release the datasets here. And We hope it can be a basis for possible follow-up research, which requires accurate mapping between CVEs and patches. Although we have tried best to ensure its accuracy, mistakes still be possible. If you find anything wrong, please kindly report an issue. So many thanks for your effort!  Let's maintain it together 😄. 