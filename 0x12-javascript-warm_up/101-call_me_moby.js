#!/usr/bin/node

function callMeMoby (x, bilFunction) {
  for (let i = 0; i < x; i++) {
    bilFunction();
  }
}
module.exports = {
  callMeMoby
};
