import React, { Component } from 'react';

class SchoolComponent extends Component {

	constructor(props) {
		super(props);
		this.state = {

		};
	}

	render() {
		return (
	    	<div className="layout">
		      	<h1>{this.props.school}</h1>
	        </div>
	    );
    }
}

export default SchoolComponent;