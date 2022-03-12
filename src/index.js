/*
Info
Name: ZoomFcker
Version: 1.1
Author: Dumpy
Repo: https://github.com/dumpydev/zoomfcker

*/

const os = require("os");
const path = require("path");
const fs = require("fs");
const { exec } = require("child_process");
var colors = require('colors');

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

var platform = os.platform();
var home = os.homedir();

var zoompath = path.join(home, "AppData", "Roaming", "Zoom");

function main() {
    console.log(`
    --------------------------------
    |      ZOOM ZOOM BYE BYE       |
    |              V1              |
    --------------------------------
    `.rainbow)   

  deleteZoom();
  
}

function deleteZoom() {
  if (platform.toLocaleLowerCase() === "darwin") {
    console.log("MacOS");
  } else if (platform.toLocaleLowerCase() === "win32") {
    fs.rmdir(zoompath, () => {
      console.log(`
      ----------------
      | Zoom Deleted |
      ----------------
      `.red);
    });
  }
}

main();
