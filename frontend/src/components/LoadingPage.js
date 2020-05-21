import React from 'react';

class LoadingPage extends React.Component {
    render() {
        return (
            <div className='loader'>
                <img src='/images/loader.gif' className='loader__image' />
            </div>
        )
    }
}

export default LoadingPage;