const INPUT_FILE = process.platform === 'linux' ? '/dev/stdin' : './input';
const [targetTime, min, max, increase, decrease] = require('fs')
  .readFileSync(INPUT_FILE)
  .toString()
  .trim()
  .split(' ')
  .map(Number);

let time;
let exerciseTime = 0;
let heartbeat = min;

for (time = 0; exerciseTime < targetTime; time += 1) {
  if (min + increase > max) break;
  if (heartbeat + increase <= max) {
    heartbeat += increase;
    exerciseTime += 1;
  } else {
    heartbeat = Math.max(min, heartbeat - decrease);
  }
}

console.log(exerciseTime === targetTime ? time : -1);