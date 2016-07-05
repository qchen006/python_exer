'''
Created on 2016/05/22

/**
<(?<tag>[^\s>]+)[^>]*>(.|\n)*?</\k<tag>>
*/

@author: hadoop
'''

import re
regexStr = "<(S*?)[^>]*>.*?|<.*?/>"
htmlContent = """
<div style="background-color:gray;" id="footer"> </div>
   
"""
   
result = re.search(regexStr, htmlContent, 
              re.M|re.I) 
print result.groups()