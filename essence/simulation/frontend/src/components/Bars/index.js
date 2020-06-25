import React from 'react';
import * as d3 from 'd3';
import styles from './style';

export default class Bars extends React.PureComponent {
  constructor(props) {
    super(props);
    this.references = { stats1: React.createRef(), stats2: React.createRef(), text1: React.createRef(), text2: React.createRef(), text3: React.createRef(), text4: React.createRef() };
  }

  componentDidMount() {
    this.animate();
  }

  componentDidUpdate() {
    this.animate();
  }

  animate() {
    switch (this.props.phase) {
      case 1:
          this.animatePhase1();
          break;
      case 2:
        this.animatePhase2();
        break;
      default:
          // do nothing
    }
  }

  animatePhase1() {
    d3.select(this.references.text1.current)
        .style('opacity', 0)
    d3.select(this.references.text2.current)
        .style('opacity', 0)
    d3.select(this.references.text3.current)
        .style('opacity', 0)
    d3.select(this.references.text4.current)
        .style('opacity', 0)
  }

  animatePhase2() {
    const { duration, percentageWhite, percentageBlack } = this.props;
    const steps = 4;
    const timePerStep = duration / steps;
    const delay = timePerStep * 0.5;
    const animationTime = timePerStep * 0.25;
    
    d3.select(this.references.stats1.current)
        .transition()
        .delay(timePerStep * 3)
        .transition()
        .delay(delay)
        .duration(animationTime)
        .attr('height', `${percentageWhite}%`)

    d3.select(this.references.stats2.current)
        .transition()
        .delay(timePerStep * 3)
        .transition()
        .delay(delay)
        .duration(animationTime)
        .attr('height', `${percentageBlack}%`)

    d3.select(this.references.text1.current)
        .transition()
        .delay(timePerStep * 3)
        .transition()
        .delay(delay)
        .duration(animationTime)
        .style('opacity', 1.0)

    d3.select(this.references.text2.current)
        .transition()
        .delay(timePerStep * 3)
        .transition()
        .delay(delay)
        .duration(animationTime)
        .style('opacity', 1.0)

    d3.select(this.references.text3.current)
        .transition()
        .delay(timePerStep * 3)
        .transition()
        .delay(delay)
        .duration(animationTime)
        .style('opacity', 1.0)

    d3.select(this.references.text4.current)
        .transition()
        .delay(timePerStep * 3)
        .transition()
        .delay(delay)
        .duration(animationTime)
        .style('opacity', 1.0)
  }

  render() {
    return (
        <g>
            <g style={styles.barContainer1}>
                <rect ref={this.references.stats1} style={styles.bar}
                    x='0'
                    y='0'
                    width='6%'
                    height='0'
                    fill='#2396CD'
                    strokeWidth='0'
                />
                <text ref={this.references.text1} x='0' y='-1%' style={styles.text}>
                    {Math.round(this.props.percentageWhite)}%
                </text>
                <text ref={this.references.text2} x='0' y='3%' style={styles.text2}>
                    Wit
                </text>
            </g>
            <g style={styles.barContainer2}>
                <rect ref={this.references.stats2} style={styles.bar}
                    x='0'
                    y='0'
                    width='6%'
                    height='0'
                    fill='#2396CD'
                    strokeWidth='0'
                />
                <text ref={this.references.text3} x='0' y='-1%' style={styles.text}>
                    {Math.round(this.props.percentageBlack)}%
                </text>
                <text ref={this.references.text4} x='0' y='3%' style={styles.text2}>
                    Zwart
                </text>
            </g>
        </g>
    );
  }
}
