import ColorConverter from '../utils/ColorConverter';
import { Component } from 'react';

import styles from './Button.module.css';

class Button extends Component {
             
    constructor(props) {
        super(props);

        let style = props.style || {}

        style.background ||= '#AAA';
        style.borderColor ||= style.background;
        style.color ||= 'white';
        
        style.backgroundHover ||= ColorConverter.subtractColors(style.background, [30, 30, 30]);
        style.borderColorHover ||= style.backgroundHover;
        style.colorHover ||= style.color;

        style.backgroundActive ||= ColorConverter.subtractColors(style.backgroundHover, [30, 30, 30]);
        style.borderColorActive ||= style.backgroundActive;
        style.colorActive ||= style.color;

        this.state = {
            ...style,
            background: style.background,
            borderColor: style.borderColor,
            color: style.color,
        };

        this.style = style;
        this.children = props.children;

        this.handleMouseEvent = this.handleMouseEvent.bind(this);
        this.onClick = props.onClick.bind(props.parent);

        // this.state.onClick = this.onClick;
    }

    handleMouseEvent(event) {
        switch (event.type) {
            case "mousedown":
                this.setState({
                    ...this.style,
                    background: this.style.backgroundActive,
                    borderColor: this.style.borderColorActive,
                    color: this.style.colorActive,
                    onClick: this.state.onClick,
                })
                break
            case "mouseleave":
                this.setState({
                    ...this.style,
                    background: this.style.background,
                    borderColor: this.style.borderColor,
                    color: this.style.color,
                    onClick: this.state.onClick,
                })
                break;
            case "mouseenter":
            case "mouseup":
                this.setState({
                    ...this.style,
                    background: this.style.backgroundHover,
                    borderColor: this.style.borderColorHover,
                    color: this.style.colorHover,
                    onClick: this.state.onClick,
                })
                break;
        }
    }

    render() {
        return (
            <button 
                {...this.props}
                style={this.state}

                onMouseDown={this.handleMouseEvent}
                onMouseUp={this.handleMouseEvent}
                onMouseEnter={this.handleMouseEvent}
                onMouseLeave={this.handleMouseEvent}
            >
                {this.children}
            </button>
        );
    }
}


export default Button;