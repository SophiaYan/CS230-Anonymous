start     = _ open _ nodes:node* _ close _                { return nodes; }
node      = open _ type:famixtype _ attrs:attr* _ close _ { return MSE.createNode(type, attrs);  }
famixtype = "FAMIX." typename:chars                       { return typename; }
ref       = open _ "ref:" _ id:int _ close _              { return { ref: id }; }
attr      = open _ name:name _ values:value* _ close _    { return { name: name, values:values }; }
value     = chars / string / ref
open      = '('
close     = ')'
string    = del str:([^\'\" \t\n\r] / [ ])* del           { return str.join(""); }
del       = "'" / '"'
name      = chars:[^:()\'\" \t\n\r]+[:]?                  { return chars.join(""); }
chars     = chars:char+                                   { return chars.join(""); }
char      = [^()\'\" \t\n\r]
int       = digits:[0-9]+                                 { return parseInt(digits.join(""), 10); }
_         = space*
space     = [ \t\n\r]
