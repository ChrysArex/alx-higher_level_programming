#!/usr/bin/node
let greatest = parseInt(process.argv[2]);
let Bgreatest = parseInt(process.argv[2]);
const args = process.argv;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    if (args[i] > greatest) {
      Bgreatest = greatest;
      greatest = args[i];
    }
  }
  console.log(Bgreatest);
}
