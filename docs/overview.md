# overview
Fern is a simple language that transpiles into js.

## importing 

use math
use threejs
use custom-style.css as st // button.style = st.gradient // just copies from the style file
use elements-snippets.html as sn // button.innerhtml = sn.flashy-button // just coppies the scope from html

## vars
int x 
int y = 9
str name
### basic types
bool
int uint
float
auto // no type, the default js
null // null type
err // error is a type
fn // function is a callable type
obj // object type, basically js const but for DOM elements
### type modifications
const // make it constant
temp // make it single use
secret // encrypted only when read
pub // make it global
local // for the current module use only
owned .. <foo(), bar()> // only allowed to be read by pre-defined functions
shared // safe to share between threads and async calls
opt // can return type or null or err

##### mods stacking
mod's order is up to you, but owned must follow it's grammar.
pub secret int key // order mods as you like
owned opt bool flag <foo()> // owned's <args> must always be at the end.

### type crafting
#### dynamic types
for when you're not sure whither the return type is a or b
use dtype to create a simple dynamic type on the fly
dtype <str| int| err> result // for creating complex types
secret dtype <int| str> result // outside mods apply to all inner types
dtype <opt int| temp str> result // you can use mods on the primitive types within dtype

use typedef <> to create a reusable dtype
typedef dtype <> apiR
  opt str
  temp secret int
  err
end

apiR weatherResult
#### structs
struct point2d // struct like any other lang
  int x
  int y
end
point2d playerPosition

#### enums
// type-less enums are always ints and start from 0, you can assign different values to them
enum serverr
  ok
  connectionError
  timeOut
  wrongResponse
  unexpected
end
serverr fetchErr // fetchErr can only equal one of the enum elements
int x = fetchErr::ok // enums are accessed via ::

// define an enum type
enum <str> color
  white = "#ffffff"
  black = "#000000"
  grey = "#050000"
end

btn.style.color = color::white


## functions 
### typical function
fn foo(int bar) -> int
  // do something
  return bar2
end

### simple function
fn foo()
  // do something
end

### lambda functions
int x(y, z) -> (y + z * 10) / 2 // these are always a single type functions
bool j(n, y) -> n && t 
str mix(name1, name2) -> name1[0] + name2[0] + name1[:0]
fn btn(arg) -> foo(arg) bar(arg) // fn is a callable type. This can only call functions, never returns a thing.

## control flow 
### if else 
#### simple if else

if x == 0
  // do something
else
  // do something
end

// if else
if y == 0
  // do something
else if y == 1 
  // do something
else 
  // do something
end
#### single liner aka ternary ops
int x 
x(name == "Tim") = 22 else 19
str group(age < 18) = "child" else "adult"
int secret(encrypt_flag) = hash(id) else id // you can call functions in conditional assignments

#### switch statements
str msg
switch arch
  case "arm32"
    msg = "32 bit"
  case "amd64", "wasm64p32", "arm64" // you can have multiple case checks
    msg = "64 bit"
  case other // the other keyword is the default fallback
    msg = "unknow architecture"
end

#### loops
##### for loop
int[] list = \[1 .. 10]
for i in list
  // do something
end

// or more simply
for i in \[1 .. 100]
  // do something
end

##### while loop
// simple while
while flag 
  // do something
end

// complex while
while i(i < 10) = i+2 // while checks for the internal condition
  // do something
end



## unique features

### tiny features
#### DOM elements mapping
map plybtn to objwithId('player') // simply map to DOM elements

map // batch map
  nxtbtn objwithId('next')
  prvbtn objwithId('previous')
  pusbtn objwithId('pause')
end

#### string formatting
str greet = f"hello {userName}" // python style formatting

#### eval 
eval r of fetch(url)
  ? json >> response_parse(r) ? err >> parse_error(err) // if fn returns err, you must handle it in every call
  ? err >> fetch_error(err)

### raw js 
// simple raw
raw
  // write your raw js code here
end

### debug annotations
? val, read, call, trace, mut, type

### compile-time directives aka less ugly macros
#unroll (unrolls a loops and switches)
#defer (like odin's)
