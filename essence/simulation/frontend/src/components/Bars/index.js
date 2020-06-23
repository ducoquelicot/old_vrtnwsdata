import React from 'react';
import * as d3 from 'd3';
import styles from './style';

export default class Bars extends React.PureComponent {
  constructor(props) {
    super(props);
    this.references = { stats1: React.createRef(), stats2: React.createRef() };
  }

  componentDidMount() {
    this.animate();
  }

  componentDidUpdate() {
    this.animate();
  }

  animate() {
    switch (this.props.phase) {
      case 2:
        this.animatePhase2();
        break;
    }
  }

  animatePhase2() {
    const { percentageWhite, percentageBlack } = this.props;

    console.log(percentageBlack, percentageWhite);
    
    d3.select(this.references.stats1.current)
        .transition()
        .delay(5000)
        .duration(1000)
        .attr('height', `${percentageWhite}%`)

    d3.select(this.references.stats2.current)
        .transition()
        .delay(5000)
        .duration(1000)
        .attr('height', `${percentageBlack}%`)
  }

  render() {

    return (
        <g>
            <g style={styles.barContainer1}>
                <rect ref={this.references.stats1} style={styles.bar}
                    x='0'
                    y='0'
                    width='5%'
                    height='10'
                    fill='#2396CD'
                    strokeWidth='0'
                />
                <text x='0' y='10%'>
                    {this.props.whitePercentage}
                </text>
            </g>
            <g style={styles.barContainer2}>
                <rect ref={this.references.stats2} style={styles.bar}
                    x='0'
                    y='0'
                    width='5%'
                    height='10'
                    fill='#2396CD'
                    strokeWidth='0'
                />
            </g>
        </g>
    );
  }
}
