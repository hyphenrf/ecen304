import React from 'react';
import moment from 'moment';
import { SingleDatePicker } from 'react-dates';
import 'react-dates/initialize';
import 'react-dates/lib/css/_datepicker.css';

class AuthorForm extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      name: props.author ? props.author.name : '',
      dateOfBirth: props.author ? moment(props.author.dateOfBirth) : moment(),
      listOfBooks: props.author ? props.author.listOfBooks : [],
      Genre: props.author ? props.author.genre : [],
      calendarFocused: false,
      error: ''
    };
  };
  onNameChange = (e) => {
    const name = e.target.value;
    this.setState(() => ({ name }));
  };
  onDateChange = (dateOfBirth) => {
    if (dateOfBirth) {
      this.setState(() => ({ dateOfBirth }));
    }
  };
  onSubmit = (e) => {
    e.preventDefault();

    if (!this.state.name) {
      this.setState(() => ({ error: 'Please enter all required Data' }));
    } else {
      this.setState(() => ({ error: '' }));
      this.props.onSubmit({
        name: this.state.name,
        dateOfBirth: this.state.dateOfBirth,
        listOfBooks: this.state.listOfBooks,
        Genre: this.state.Genre
      });
    }
  };

  render() {
    return (
      <form onSubmit={this.onSubmit}>
        {this.state.error && <p>{this.state.error}</p>}
        <input
          type="text"
          placeholder="Name"
          autoFocus
          value={this.state.name}
          onChange={this.onNameChange}
        />

        <SingleDatePicker
          date={this.state.dateOfBirth}
          onDateChange={this.onDateChange}
          focused={this.state.calendarFocused}
          onFocusChange={({ focused }) => this.setState({ calendarFocused: focused })}
          numberOfMonths={1}
          isOutsideRange={() => false}
        />
        <div>
          <button>Save</button>
        </div>
      </form>
    )
  }
};

export default AuthorForm;