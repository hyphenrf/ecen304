import React from 'react';
import Modal from 'react-modal';

class BookModal extends React.Component {
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
            contentLabel='Book Modal'
            closeTimeoutMS={200}
            className="modal"
        >
            <h1>{props.book.name}</h1>
            {props.book.genre === 0 && <h3>List of Genre's is currently unavialable!</h3>}
            {
                props.book.genre.map((genre, index) => (
                    <h3>{genre},</h3>
                ))
            }

            <button className='btn' onClick={this.closeModal}>Close</button>
        </Modal>
    }
};

// ---------------------- Make book key -----------------------

export default BookModal;