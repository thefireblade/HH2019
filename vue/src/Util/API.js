import axios from "axios";
import { URLs } from "../Config";

function getAllFood(callback) {
  const url = URLs.API_BASE_URL + URLs.ALL_ITEMS;

  axios
    .get(url)
    .then(response => {
      callback(response.data);
    })
    .catch(error => {
      console.log(error);
    });
}

function getFood(url, callback) {
  const reset_url = URLs.API_BASE_URL + URLs.RESET;
  console.log(reset_url);
  axios.get(reset_url, response => {
    console.log(response.data.Success);
  });

  setTimeout(() => {
    axios
      .get(url)
      .then(data => {
        console.log("called back");
        callback(data.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, 3000);
}

// This assume the location has already been retrieved in the temp table.
function sortBy(less_than, field, amount, callback) {
  let type;
  if (less_than) {
    type = "lessthanequalto";
  } else {
    type = "greaterthan";
  }

  const URL = `${URLs.API_BASE_URL}/api/sort/${type}/${field}/${amount}.0`;

  axios.get(URL).then(response => {
    callback(response.data);
  });
}

export default {
  getAllFood,
  getFood,
  sortBy
};
