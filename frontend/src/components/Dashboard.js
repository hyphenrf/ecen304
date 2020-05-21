import React from 'react';
import { Link } from 'react-router-dom';

class Dashboard extends React.Component {
    render() {
        return (
            <div>
                <Link to='/create/Author'>create author</Link><br />
                <Link to='/create/Book'>create Book</Link><br />
                <input
                    type="text"
                    placeholder="Choose your poison?"
                    autoFocus
                />
                <Link to=''>View all toxins?</Link>
            </div>
        )
    }
}

export default Dashboard;