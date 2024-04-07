from IPython.display import HTML
import pandas as pd
import json
import os



rootpath = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    return open(os.path.join(rootpath, *parts)).read()

def add_one(number):
    return number + 1


def print2(df,count_row = 110,save_result_html=False):
    lsCols = []
    for c in df.columns:
        lsCols.append({ 'field' : c})
    
    _columns = json.dumps(lsCols)
    _dataset = df.head(count_row).to_json(orient = 'records')
    
    temp1 = """
<div id="MyGridContiner1" style="width:100%;height:550px; background-color:#fff; padding: 0px; margin:0;">
        <script>
            var on_full_screen = false;
            function fun1(el){
                if(on_full_screen == false)
                {
                    let _ElDiv = el.parentElement; 
                    openFullscreen(_ElDiv);
                    on_full_screen = true;
                }
                else
                {
                    closeFullscreen()
                    on_full_screen = false;
                }
                
                
            }

            

            function openFullscreen(elem) {
              if (elem.requestFullscreen) {
                elem.requestFullscreen();
              } else if (elem.webkitRequestFullscreen) { /* Safari */
                elem.webkitRequestFullscreen();
              } else if (elem.msRequestFullscreen) { /* IE11 */
                elem.msRequestFullscreen();
              }
            }

            function closeFullscreen() {
              if (document.exitFullscreen) {
                document.exitFullscreen();
              } else if (document.webkitExitFullscreen) { /* Safari */
                document.webkitExitFullscreen();
              } else if (document.msExitFullscreen) { /* IE11 */
                document.msExitFullscreen();
              }
            }
        </script>
<div id="MyGrid1" style="width:100%;height:550px;border:none;padding:0px;margin:0px;top:0px;left:0px;z-index: 100;">
<img style="position:absolute;z-index:10;right:7px;top:7px;width: 24px;height:24px;border:1px solid #aaaaaa66;background-color:#aaaaaa22;cursor:pointer;color:wheat;" title="Full Screen"
onclick="fun1(this);" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAABBUlEQVR4nO3ZXwoCIRAGcKGOsU7XqYjqrc7YJaJxz1EPtf177AJfyEr0uLaWEt8PfB0dHHBUY4iI/oI4IGZYh8PIYdI1fqVYW8U1dh7z7UTCOHYKvsXQKh6fzGGKSmSDQbGJWId9pRh3jW9rrLKUlslEmEjAHUlMWFoBSysxYWkFvnd6P+xMJqJoXruiOEUH8A2gbzn8iDmxU7M7LMTh7rsAW2Oeax1EREREKVWKZehxbjl7nKrvOnp3nYlI33XwhpiY8IYYsLQSE5ZWwNJKTH7+0aNoYk7eUY3p+5NTMR890r5/XTrHV5yK/LGSNpFzRPxjmYkoGlHMYh4A/Qvm1xMhov/yBFS8Q63uf8nyAAAAAElFTkSuQmCC"
/>
<iframe srcdoc="HTML_CONTENT" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe>
</div></div>
"""


    
    html_code = read('index_AGG.html')
    
    k1 = '&quot;'
    k2 = '&lt;'
    k3 = '&gt;'
    html_code = html_code.replace('_DATASET_',_dataset).replace('_COLUMNS_',_columns)
    
    if save_result_html == True:
      with open("index_AGG_result.html", "w") as file:
          file.write(html_code)
    
    html_code = html_code.replace('"',k1).replace('<',k2).replace('>',k3)
    tempHtml = temp1.replace("HTML_CONTENT",html_code)

    return HTML(tempHtml)
    
