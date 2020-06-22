import React from 'react';
import * as d3 from 'd3';

export default class Titles extends React.PureComponent {
  constructor(props) {
    super(props);
    this.references = { citizen: React.createRef() };
  }

  componentDidMount() {
    this.showCitizen();
  }

  showCitizen() {
    const { delay } = this.props;

    d3.select(this.references.citizen.current)
      .style('opacity', 0)
      .transition()
      .delay(delay)
      .duration(1000)
      .style('opacity', 1.0);
  }

  render() {
    const { skinTone, guilty } = this.props;
    return (
      <circle ref={this.references.citizen}
        cx={`${Math.round(Math.random() * 90) + 5}%`}
        cy={`${Math.round(Math.random() * 90) + 5}%`}
        r="0.75%"
        stroke={guilty ? 'red' : 'black'}
        fill={skinTone}
      />
    );
  }
}
