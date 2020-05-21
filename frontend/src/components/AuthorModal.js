import React from 'react';
import Modal from 'react-modal';

class AuthorModal extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            modalIsOpen: undefined
        }
    };

    openModal = () => {
        this.setState(() => ({ modalIsOpen: true }));
    };

    closeModal = () => {
        this.setState(() => ({ modalIsOpen: false }));
    };

    render() {
        <Modal
            isOpen={!!this.state.modalIsOpen}
            onRequestClose={!!this.state.modalIsOpen}
            contentLabel='Author Modal'
            closeTimeoutMS={200}
            className="modal"
        >
            <h1>{props.author.name}</h1>
            {props.author.genre === 0 && <h3>List of Genre's is currently unavialable!</h3>}
            {
                props.author.genre.map((genre, index) => (
                    <h3>{genre},</h3>
                ))
            }

            <button className='btn' onClick={this.closeModal}>Close</button>
        </Modal>
    }
};

// ---------------------- Make author key -----------------------

export default AuthorModal;