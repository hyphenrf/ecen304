import React from 'react';
import { Link } from 'react-router-dom';
import Auth from './Authorization'

class Header extends React.Component {
    render() {
        return (
            <div>
                <Link to='/' >BookClub</Link>
                <Auth />
            </div>
        )
    }
}

export default Header;