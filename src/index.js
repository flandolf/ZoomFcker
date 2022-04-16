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
const figlet = require("figlet");
const { exec } = require("child_process");
var colors = require("colors");

const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

var platform = os.platform();
var home = os.homedir();

var zoompath = path.join(home, "AppData", "Roaming", "Zoom");

function main() {
  figlet("Zoom-F", function (err, data) {
    if (err) {
      console.log("Something went wrong...");
      console.dir(err);
      return;
    }
    console.log(data);
  });

  deleteZoom();
}

function deleteZoom() {
  if (platform.toLocaleLowerCase() === "darwin") {
    fs.rmdir(path.join('Applications', 'zoom.us'), () => {
      console.log('Something went wrong...')
    })
    console.log("MacOS not supported.... Sorry!");
    rl.question("", function (answer) {
      rl.close();
    });
  } else if (platform.toLocaleLowerCase() === "win32") {
    fs.rmdir(zoompath, () => {
      figlet("Zoom Deleted.", function (err, data) {
        if (err) {
          console.log("Something went wrong...");
          console.dir(err);
          return;
        }
        console.log(data);
      });
      rl.question("".rainbow, function (answer) {
        rl.close();
      });
    });
  }
}

main();
