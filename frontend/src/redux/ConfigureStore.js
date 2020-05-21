import { createStore, combineReducers, compose, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import authorsReducer from './Reducers/Authors';
import booksReducer from './Reducers/Books';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

export default () => {
    const store = createStore(
        combineReducers({
            authors: authorsReducer,
            books: booksReducer
        }),
        composeEnhancers(applyMiddleware(thunk))
    );

    return store;
};
