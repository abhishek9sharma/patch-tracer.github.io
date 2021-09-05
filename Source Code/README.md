# Tracer Prototype

**Tracer** is an automated approach to find patches for open source software OSS vulnerabilities. The key idea is that patch commits will be frequently referenced during the reporting, discussion, and resolution of an OSS vulnerability. Thus, Tracer finds patches in the way of constructing a reference network. 

### Environment Configuration 

* Python: 3.6.2

The dependencies are listed in the **requirements.txt**. Please install them as follows. 

```cmd
$ cd $WORKDIR$/tracer-master/
$ pip install -r requirements.txt
```

### Quick Start

1. download NVD dataset

   ~~~cmd
   $ cd $WORKDIR$/tracer-master/data/
   $ python download_and_parse_NVD.py
   ~~~

   output:

   ```cmd
   ... finish download_NVD_data_feed()
   ... finish separateCVEItems()
   ```

2. run Tracer 

   ```cmd
   $ cd $WORKDIR$/tracer-master/vulnerability_analysis/patch_localization/tool/
   $ python tool_in_formal.py $cveid$ $network_pic_path$
   ```

   cveid: the CVE you are finding patches for

   network_pic_path: the path to store the picture of the reference network

   **Example: **

   * CVE-2017-16016

   ```cmd
   $ python tool_main.py CVE-2017-16016 ./CVE-2017-16016_network.pdf
   ```

   * output

   ```cmd
   ##### OUTPUT #####
   The localized patches for CVE-2017-16016 are: 
   https://github.com/punkave/sanitize-html/commit/5d205a1005ba0df80e21d8c64a15bb3accdb2403
   
   The network picture has been stored. Path: ./CVE-2017-16016.pdf
   ```

### Update

If you have any questions or issues, please feel free to report an issue. We will continue to maintain this project. Thanks for your feedback😄. 
