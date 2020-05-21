import React from 'react';
import moment from 'moment';
import { SingleDatePicker } from 'react-dates';
import 'react-dates/initialize';
import 'react-dates/lib/css/_datepicker.css';

class BookForm extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            name: props.book ? props.book.name : '',
            author: props.book ? props.book.author : '',
            type: props.book ? props.book.type : '',
            genre: props.book ? props.book.genre : '',
            description: props.book ? props.book.name : '',
            ISBN: props.book ? props.book.ISBN : 0,
            edition: props.book ? props.book.edition : 1,
            price: props.book ? props.book.price : 0,
            NumOfAvailableCopies: props.book ? props.book.NumOfAvailableCopies : 0,
            NumOfPages: props.book ? props.book.NumOfPages : 0,
            dateOfPublication: props.book ? moment(props.book.dateOfPublication) : moment(),
            pictures: [],
            calendarFocused: false,
            error: ''
        };
    };

    onNameChange = (e) => {
        const name = e.target.value;
        this.setState(() => ({ name }));
    };
    onAuthorChange = (e) => {
        const author = e.target.value;
        this.setState(() => ({ author }));
    };
    onTypeChange = (e) => {
        const type = e.target.value;
        this.setState(() => ({ type }));
    };
    onGenreChange = (e) => {
        const genre = e.target.value;
        this.setState(() => ({ genre }));
    };
    onDescriptionChange = (e) => {
        const description = e.target.value;
        this.setState(() => ({ description }));
    };
    onISBNChange = (e) => {
        const ISBN = e.target.value;
        this.setState(() => ({ ISBN }));
    };
    onEditionChange = (e) => {
        const edition = e.target.value;
        this.setState(() => ({ edition }));
    };
    onPriceChange = (e) => {
        const price = e.target.value;
        this.setState(() => ({ price }));
    };
    onCopiesChange = (e) => {
        const NumOfAvailableCopies = e.target.value;
        this.setState(() => ({ NumOfAvailableCopies }));
    };
    onPagesChange = (e) => {
        const NumOfPages = e.target.value;
        this.setState(() => ({ NumOfPages }));
    };
    onDateChange = (dateOfPublication) => {
        if (dateOfPublication) {
            this.setState(() => ({ dateOfPublication }));
        }
    };
    onSubmit = (e) => {
        e.preventDefault();

        if (!this.state.name || !this.state.author || this.state.pictures.length === 0) {
            this.setState(() => ({ error: 'Please enter all required Data' }));
        } else {
            this.setState(() => ({ error: '' }));
            this.props.onSubmit({
                name: this.state.name,
                author: this.state.author,
                type: this.state.type,
                genre: this.state.genre,
                description: this.state.description,
                ISBN: this.state.ISBN,
                edition: this.state.edition,
                price: this.state.price,
                NumOfAvailableCopies: this.state.NumOfAvailableCopies,
                NumOfPages: this.state.NumOfPages,
                dateOfPublication: this.state.dateOfPublication,
                pictures: this.state.pictures
            });
        }
    };

    render() {
        return (
            <form onSubmit={this.onSubmit}>
                {this.state.error && <p>{this.state.error}</p>}
                <input
                    type="text"
                    placeholder="Book Name"
                    autoFocus
                    value={this.state.name}
                    onChange={this.onNameChange}
                />
                <input
                    type="text"
                    placeholder="Author Name"
                    value={this.state.author}
                    onChange={this.onAuthorChange}
                />
                <input
                    type="text"
                    placeholder="Genre"
                    value={this.state.genre}
                    onChange={this.onGenreChange}
                />
                <input
                    type="text"
                    placeholder="Type"
                    value={this.state.type}
                    onChange={this.onTypeChange}
                />
                <input
                    type="number"
                    placeholder="Edition"
                    value={this.state.edition}
                    onChange={this.onEditionChange}
                />
                <input
                    type="number"
                    placeholder="ISBN"
                    value={this.state.ISBN}
                    onChange={this.onISBNChange}
                />
                <input
                    type="number"
                    placeholder="Price"
                    value={this.state.price}
                    onChange={this.onPriceChange}
                />
                <input
                    type="number"
                    placeholder="# Pages"
                    value={this.state.NumOfPages}
                    onChange={this.onPagesChange}
                    required
                />
                <input
                    type="number"
                    placeholder="# of Available copies"
                    value={this.state.NumOfAvailableCopies}
                    onChange={this.onCopiesChange}
                />
                <SingleDatePicker
                    date={this.state.dateOfPublication}
                    onDateChange={this.onDateChange}
                    focused={this.state.calendarFocused}
                    onFocusChange={({ focused }) => this.setState({ calendarFocused: focused })}
                    numberOfMonths={1}
                    isOutsideRange={() => false}
                />
                <textarea
                    type="text"
                    placeholder="Description"
                    value={this.state.description}
                    onChange={this.onDescriptionChange}
                />
                <div>
                    <button>Save</button>
                </div>
            </form>
        )
    }
};

export default BookForm;