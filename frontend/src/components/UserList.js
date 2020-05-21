import React from 'react';
import { connect } from 'react-redux';

export class UserList extends React.Component {
  constructor(props) {
    super(props);
  };

  render() {
    return (
      <div>
        <div>
          <div>Users</div>
          <div>User</div>
        </div>
        {
          props.users.length === 0 ? (
            <p>No Users yet!</p>
          ) : (
              props.users.map((user) => {
                return (
                  <div>
                    <h3>{user.Uname}</h3>
                    <h3>{user.description}</h3>
                  </div>
                )
              })
            )
        }
      </div>
    )
  };
};

const mapStateToProps = (state) => {
  return {
    users: selectUsers(state.users, state.filters)
  };
};

export default connect(mapStateToProps)(UserList);
