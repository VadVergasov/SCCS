import { makeAutoObservable } from 'mobx';


export default class CardStore {
    constructor() {
        this._cards = [];

        this._authors = [];
        this._categories = [];
        this._pattern = "";

        this._selectedAuthor = null;
        this._selectedCategory = null;

        makeAutoObservable(this);
    }

    setAuthors(authors) {
        this._authors = authors;
    }

    setCategories(categories) {
        this._categories = categories;
    }

    setCards(cards) {
        this._cards = cards;
    }

    selectAuthor(author) {
        this._selectedAuthor = author;
    }

    selectCategory(category) {
        this._selectedCategory = category;
    }

    setPattern(pattern) {
        this._pattern = pattern;
    }

    get cards() {
        return this._cards;
    }

    get authors() {
        return this._authors;
    }

    get categories() {
        return this._categories;
    }

    get selectedAuthor() {
        return this._selectedAuthor;
    }

    get selectedCategory() {
        return this._selectedCategory;
    }

    get pattern() {
        return this._pattern;
    }

}