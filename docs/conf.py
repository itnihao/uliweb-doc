#coding=utf8

"""
This config will be used for parm project settings.
You can change them to fit your needs.
"""

#available plugins
plugins = []

# The suffix of source filenames.
source_suffix = ['.md', '.markdown']

#template setttings
template_dirs = "_build"
templates = {'index':'index.html', '*':'default.html'}

tag_class = {
    'table':'table table-bordered',
    'pre':'prettyprint linenums',
}

# pre code theme css only : sons-of-obsidian, sunburst
# can be found in static/asset directory
pre_css = 'sons-of-obsidian'

# General information about the project.
project = u'Uliweb-Doc'
project_url = './index.html'
copyright = u'2013, Limodou'
# You can add custom css files, just like
# custom_css = ['/static/custom.css']
custom_css = []
# The short X.Y version.
version = '0.2'

# config menus
# format: ('name', 'caption', 'link')
menus = [
    ('home', 'Home', 'index.html'),
]

# in content footer you can config comment tool just like disque
content_footer = ''

#page footer
footer = """<footer class="footer">
  <div>
    <p>Designed by Limodou, Copyright %s</p>
    <p>CSS framework <a href="https://github.com/twitter/bootstrap">Bootstrap</a>, Markdown parser lib <a href="https://github.com/limodou/par">Par</a> and this page is created by <a href="https://github.com/limodou/parm">Parm</a> tool.</p>
  </div>
</footer>
""" % copyright

# The master toctree document.
master_doc = 'index'

#download source display
download_source = 'View Source'

#disqus
disqus_text = '''<div id="disqus_thread" style="margin:20px;"></div>
 <script type="text/javascript">
     /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
     var disqus_shortname = 'uliwebdoc'; // required: replace example with your forum shortname

     /* * * DON'T EDIT BELOW THIS LINE * * */
     (function() {
         var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
         dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
         (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
     })();
 </script>
 <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
 <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>
'''

disqus_js = '''<script type="text/javascript">
   /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
   var disqus_shortname = 'uliwebdoc'; // required: replace example with your forum shortname

   /* * * DON'T EDIT BELOW THIS LINE * * */
   (function () {
       var s = document.createElement('script'); s.async = true;
       s.type = 'text/javascript';
       s.src = 'http://' + disqus_shortname + '.disqus.com/count.js';
       (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
   }());
   </script>
'''
