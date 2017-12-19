from IPython.display import HTML
# NOTE: None of these method would work when you load IPython on GitHub. They only works when you load IPython locally or
# load as HTML

# hide Ipython warnings, you need to click "here" at the bottom
HTML('''<script>
code_show_err=false; 
function code_toggle_err() {
 if (code_show_err){
 $('div.output_stderr').hide();
 } else {
 $('div.output_stderr').show();
 }
 code_show_err = !code_show_err
} 
$( document ).ready(code_toggle_err);
</script>
To toggle on/off output_stderr, click <a href="javascript:code_toggle_err()">here</a>.''')

# hide Ipython warnings directly
HTML('''<script>
code_show_err=false; 
function code_toggle_err() {
 $('div.output_stderr').hide()
} 
$( document ).ready(code_toggle_err);
</script>''')
