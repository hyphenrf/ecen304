import React from 'react';
import createBrowserHistory from 'history/createBrowserHistory'
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Dashboard from '../components/Dashboard';
import NotFoundPage from '../components/NotFoundPage';
import AddAuthor from '../components/AddAuthor';
import EditAuthor from '../components/EditAuthor';
import AddBook from '../components/AddBook';
import EditBook from '../components/EditBook';
import Header from '../components/Header';
import Footer from '../components/Footer';

const history = createBrowserHistory()

class AppRouter extends React.Component {
    render() {
        return (
            <BrowserRouter history={history}>
                <div>
                    <Header />
                    <Switch>
                        <Route path='/' component={Dashboard} exact={true} />
                        <Route path='/create/Author' component={AddAuthor} />
                        <Route path='/create/Book' component={AddBook} />
                        <Route path="/edit/:firstName" component={EditAuthor} />
                        <Route path="/edit/:name" component={EditBook} />
                        <Route component={NotFoundPage} />
                    </Switch>
                    <Footer />
                </div>
            </BrowserRouter>
        )
    }
}

export default AppRouter;