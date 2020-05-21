// SEARCHING FILTERS
// SET_TEXT_FILTER
export const setTextFitler = (text = '') => ({
  type: 'SET_TEXT_FILTER',
  text
});

export const setAuthorNameFitler = (text = '') => ({
  type: 'SET_AUTHOR_NAME_FITLER',
  text
});

export const setBookNameFitler = (text = '') => ({
  type: 'SET_BOOK_NAME_FITLER',
  text
});


// SORTING FILTERS
export const sortByPriceAscending = () => ({
  type: 'SORT_BY_PRICE_ASCENDING'
});

export const sortByPriceDescending = () => ({
  type: 'SORT_BY_PRICE_DESCENDING'
});

export const sortByNameAscending = () => ({
  type: 'SORT_BY_NAME_ASCENDING'
});

export const sortByNameDescending = () => ({
  type: 'SORT_BY_NAME_DESCENDING'
});
