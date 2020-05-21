import React from 'react';
import { Link } from 'react-router-dom';

class NotFoundPage extends React.Component {
    render() {
        return (
            <div>
                404 - <Link to="/">Go to Dashboard</Link>
            </div>
        )
    }
}

export default NotFoundPage;