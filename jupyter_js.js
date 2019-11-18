// Code from this interesting website:
// https://www.perfectlyrandom.org/2016/03/19/sublime-text-style-multiple-cursors-in-jupyter-notebook/

require(["codemirror/keymap/sublime", "notebook/js/cell", "base/js/namespace"],function(sublime_keymap, cell, IPython) {
// setTimeout(function(){ // uncomment line to fake race-condition
cell.Cell.options_default.cm_config.keyMap = 'sublime';
var cells = IPython.notebook.get_cells();
for(var c=0; c< cells.length ; c++){
cells[c].code_mirror.setOption('keyMap', 'sublime');
}

// }, 1000)// uncomment line to fake race condition
}
);

 alert("You should be able to use Ctrl + d like in Sublime text")

