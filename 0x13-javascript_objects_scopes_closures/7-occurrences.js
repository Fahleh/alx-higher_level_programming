#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.map(
    (elem) => {
      if (elem === searchElement) {
        count += 1;
        return 1;
      } else {
        return 0;
      }
    }
  );
  return count;
};
