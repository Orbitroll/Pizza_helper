import oliveFocacciaImg from './assets/photos/olive-focaccia.png';
import gfFocacciaImg from './assets/photos/gluten-free-focaccia.png';

export const recipes = [
  { 
    id: 'ny', 
    category: 'pizza',
    nameKey: 'recipe_ny', 
    hours: 24, 
    defaultTemp: 4,
    hydration: 0.62,
    flour: 'Bread Flour (High Protein)',
    image: 'https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80',
    ingredients: [
      "1kg Caputo Chef's Flour",
      "600g Water",
      "25g Honey",
      "25g Kosher Salt",
      "20g Extra Virgin Olive Oil",
      "8g Dry Yeast",
      "Toppings: Crushed Tomatoes, Parmesan, Mozzarella"
    ],
    ingredients_he: [
      "1 ק״ג קמח קאפוטו שף",
      "600 גרם מים",
      "25 גרם דבש",
      "25 גרם מלח גס",
      "20 גרם שמן זית כתית מעולה",
      "8 גרם שמרים יבשים",
      "תוספות: עגבניות מרוסקות, פרמזן, מוצרלה"
    ],
    steps: [
      { text: "recipe_ny_step_1", duration: 2 },
      { text: "recipe_ny_step_2", duration: 3 },
      { text: "recipe_ny_step_3", duration: 3 },
      { text: "recipe_ny_step_4", duration: 3 },
      { text: "recipe_ny_step_5", duration: 60 },
      { text: "recipe_ny_step_6", duration: 15 },
      { text: "recipe_ny_step_7", duration: 120 },
      { text: "recipe_ny_step_8", duration: 1440 },
      { text: "recipe_ny_step_9", duration: 240 },
      { text: "recipe_ny_step_10", duration: 40 },
      { text: "recipe_ny_step_11", duration: 5 },
      { text: "recipe_ny_step_12", duration: 7 }
    ]
  },
  { 
    id: 'nap24', 
    category: 'pizza',
    nameKey: 'recipe_nap_24', 
    hours: 24, 
    defaultTemp: 20,
    hydration: 0.60,
    flour: '00 Flour',
    image: 'https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=600&q=80',
    ingredients: [
      "1kg Caputo \"00\" Pizzeria Flour",
      "640g Water",
      "3.5g Caputo Lievito Dry Yeast",
      "30g Salt",
      "Toppings: Ciao Tomatoes, Mozzarella, Basil"
    ],
    ingredients_he: [
      "1 ק״ג קמח קאפוטו פיצריה 00",
      "640 גרם מים",
      "3.5 גרם שמרים יבשים קאפוטו",
      "30 גרם מלח",
      "תוספות: עגבניות צ׳או, מוצרלה, בזיליקום"
    ],
    steps: [
      { text: "recipe_nap_step_1", duration: 2 },
      { text: "recipe_nap_step_2", duration: 5 },
      { text: "recipe_nap_step_3", duration: 12 },
      { text: "recipe_nap_step_4", duration: 30 },
      { text: "recipe_nap_step_5", duration: 15 },
      { text: "recipe_nap_step_6", duration: 60 },
      { text: "recipe_nap_step_7", duration: 1440 },
      { text: "recipe_nap_step_8", duration: 240 },
      { text: "recipe_nap_step_9", duration: 60 },
      { text: "recipe_nap_step_10", duration: 2 }
    ]
  },
  { 
    id: 'nap48', 
    category: 'pizza',
    nameKey: 'recipe_nap_48', 
    hours: 48, 
    defaultTemp: 4,
    hydration: 0.65,
    flour: '00 Flour (W280-320)',
    image: 'https://images.unsplash.com/photo-1595854341625-f33ee10dbf94?auto=format&fit=crop&w=600&q=80',
    ingredients: [
      "1kg Caputo \"00\" Pizzeria Flour",
      "640g Water",
      "3.5g Caputo Lievito Dry Yeast",
      "30g Salt",
      "Toppings: Ciao Tomatoes, Mozzarella, Basil"
    ],
    ingredients_he: [
      "1 ק״ג קמח קאפוטו פיצריה 00",
      "640 גרם מים",
      "3.5 גרם שמרים יבשים קאפוטו",
      "30 גרם מלח",
      "תוספות: עגבניות צ׳או, מוצרלה, בזיליקום"
    ],
    steps: [
      { text: "recipe_nap_step_1", duration: 2 },
      { text: "recipe_nap_step_2", duration: 5 },
      { text: "recipe_nap_step_3", duration: 12 },
      { text: "recipe_nap_step_4", duration: 30 },
      { text: "recipe_nap_step_5", duration: 15 },
      { text: "recipe_nap_step_6", duration: 60 },
      { text: "recipe_nap_step_7_48h", duration: 2880 },
      { text: "recipe_nap_step_8", duration: 240 },
      { text: "recipe_nap_step_9", duration: 60 },
      { text: "recipe_nap_step_10", duration: 2 }
    ]
  },
  { 
    id: 'nap72', 
    category: 'pizza',
    nameKey: 'recipe_nap_72', 
    hours: 72, 
    defaultTemp: 4,
    hydration: 0.65,
    flour: '00 Flour (Strong)',
    image: 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=600&q=80',
    ingredients: [
      "1kg Caputo \"00\" Pizzeria Flour",
      "640g Water",
      "3.5g Caputo Lievito Dry Yeast",
      "30g Salt",
      "Toppings: Ciao Tomatoes, Mozzarella, Basil"
    ],
    ingredients_he: [
      "1 ק״ג קמח קאפוטו פיצריה 00",
      "640 גרם מים",
      "3.5 גרם שמרים יבשים קאפוטו",
      "30 גרם מלח",
      "תוספות: עגבניות צ׳או, מוצרלה, בזיליקום"
    ],
    steps: [
      { text: "recipe_nap_step_1", duration: 2 },
      { text: "recipe_nap_step_2", duration: 5 },
      { text: "recipe_nap_step_3", duration: 12 },
      { text: "recipe_nap_step_4", duration: 30 },
      { text: "recipe_nap_step_5", duration: 15 },
      { text: "recipe_nap_step_6", duration: 60 },
      { text: "recipe_nap_step_7_72h", duration: 4320 },
      { text: "recipe_nap_step_8", duration: 240 },
      { text: "recipe_nap_step_9", duration: 60 },
      { text: "recipe_nap_step_10", duration: 2 }
    ]
  },
  { 
    id: 'roman', 
    category: 'pizza',
    nameKey: 'recipe_roman', 
    hours: 24, 
    defaultTemp: 4,
    hydration: 0.75,
    flour: 'Strong Bread Flour',
    image: 'https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?auto=format&fit=crop&w=600&q=80',
    ingredients: [
      "1kg Caputo \"00\" Chef's Flour",
      "750g Water (650g + 100g)",
      "5g Caputo Lievito Dry Yeast",
      "20g Salt",
      "25g Olitalia Extra Virgin Olive Oil",
      "Toppings: Roman Style Pizza Sauce, Parmesan, Mozzarella, Pepperoni"
    ],
    ingredients_he: [
      "1 ק״ג קמח קאפוטו שף 00",
      "750 גרם מים (650 + 100)",
      "5 גרם שמרים יבשים קאפוטו",
      "20 גרם מלח",
      "25 גרם שמן זית אוליטליה",
      "תוספות: רוטב פיצה רומאי, פרמזן, מוצרלה, פפרוני"
    ],
    steps: [
      { text: "recipe_roman_step_1", duration: 5 },
      { text: "recipe_roman_step_2", duration: 30 },
      { text: "recipe_roman_step_3", duration: 5 },
      { text: "recipe_roman_step_4", duration: 30 },
      { text: "recipe_roman_step_5", duration: 30 },
      { text: "recipe_roman_step_6", duration: 30 },
      { text: "recipe_roman_step_7", duration: 30 },
      { text: "recipe_roman_step_8", duration: 1440 },
      { text: "recipe_roman_step_9", duration: 15 }
    ]
  },
  { 
    id: 'sicilian', 
    category: 'pizza',
    nameKey: 'recipe_sicilian', 
    hours: 24, 
    defaultTemp: 20,
    hydration: 0.70,
    flour: 'All Purpose / Bread Mix',
    image: 'https://images.unsplash.com/photo-1561350111-7daa4f284bc6?auto=format&fit=crop&w=600&q=80',
    ingredients: [
      "1kg Flour (All Purpose / Bread Mix)",
      "700g Water",
      "10g Yeast",
      "25g Salt",
      "30g Olive Oil",
      "Toppings: Tomato Sauce, Cheese, Herbs"
    ],
    ingredients_he: [
      "1 ק״ג קמח (רב תכליתי / תערובת לחם)",
      "700 גרם מים",
      "10 גרם שמרים",
      "25 גרם מלח",
      "30 גרם שמן זית",
      "תוספות: רוטב עגבניות, גבינה, עשבי תיבול"
    ],
    steps: [
      { text: "recipe_sicilian_step_1", duration: 10 },
      { text: "recipe_sicilian_step_2", duration: 120 },
      { text: "recipe_sicilian_step_3", duration: 5 },
      { text: "recipe_sicilian_step_4", duration: 120 },
      { text: "recipe_sicilian_step_5", duration: 15 },
      { text: "recipe_sicilian_step_6", duration: 10 }
    ]
  },
  { 
    id: 'focaccia', 
    category: 'focaccia',
    nameKey: 'recipe_focaccia', 
    hours: 12, 
    defaultTemp: 20,
    hydration: 0.80,
    flour: 'Bread Flour',
    image: 'https://images.unsplash.com/photo-1573821663912-569905455b1c?auto=format&fit=crop&w=600&q=80',
    ingredients: [
      "500g Bread Flour",
      "400g Water",
      "10g Salt",
      "3g Yeast",
      "20g Olive Oil",
      "Toppings: Rosemary, Sea Salt"
    ],
    ingredients_he: [
      "500 גרם קמח לחם",
      "400 גרם מים",
      "10 גרם מלח",
      "3 גרם שמרים",
      "20 גרם שמן זית",
      "תוספות: רוזמרין, מלח ים"
    ],
    steps: [
      { text: "recipe_focaccia_step_1", duration: 5 },
      { text: "recipe_focaccia_step_2", duration: 30 },
      { text: "recipe_focaccia_step_3", duration: 30 },
      { text: "recipe_focaccia_step_4", duration: 30 },
      { text: "recipe_focaccia_step_5", duration: 240 },
      { text: "recipe_focaccia_step_6", duration: 25 }
    ]
  },
  { 
    id: 'olive_focaccia', 
    category: 'focaccia',
    nameKey: 'recipe_olive_focaccia', 
    hours: 30, 
    defaultTemp: 260,
    hydration: 0.68,
    flour: 'Caputo "00" Bread Flour',
    image: oliveFocacciaImg,
    ingredients: [
      "500g Caputo \"00\" Bread Flour",
      "340g Warm Water",
      "10g Honey",
      "2g Instant Yeast",
      "12.5g Salt",
      "15g Olitalia Extra Virgin Olive Oil",
      "Toppings: 1.5 Cups Castelvetrano Olives"
    ],
    ingredients_he: [
      "500 גרם קמח קאפוטו לחם 00",
      "340 גרם מים חמימים",
      "10 גרם דבש",
      "2 גרם שמרים אינסטנט",
      "12.5 גרם מלח",
      "15 גרם שמן זית אוליטליה",
      "תוספות: 1.5 כוסות זיתי קסטלווטראנו"
    ],
    steps: [
      { text: "recipe_olive_focaccia_step_1", duration: 5 },
      { text: "recipe_olive_focaccia_step_2", duration: 30 },
      { text: "recipe_olive_focaccia_step_3", duration: 720 },
      { text: "recipe_olive_focaccia_step_4", duration: 240 },
      { text: "recipe_olive_focaccia_step_5", duration: 60 },
      { text: "recipe_olive_focaccia_step_6", duration: 15 }
    ]
  },
  { 
    id: 'gf_focaccia', 
    category: 'focaccia',
    nameKey: 'recipe_gf_focaccia', 
    hours: 2, 
    defaultTemp: 285,
    hydration: 0.80,
    flour: 'Caputo Gluten Free Flour',
    image: gfFocacciaImg,
    ingredients: [
      "1kg Caputo Gluten Free Flour",
      "800g Water",
      "20g Caputo Lievito Dry Yeast",
      "10g Baking Soda",
      "25g Salt",
      "35g Olitalia Extra Virgin Olive Oil",
      "Toppings: Desired toppings"
    ],
    ingredients_he: [
      "1 ק״ג קמח קאפוטו ללא גלוטן",
      "800 גרם מים",
      "20 גרם שמרים יבשים קאפוטו",
      "10 גרם סודה לשתייה",
      "25 גרם מלח",
      "35 גרם שמן זית אוליטליה",
      "תוספות: תוספות רצויות"
    ],
    steps: [
      { text: "recipe_gf_focaccia_step_1", duration: 3 },
      { text: "recipe_gf_focaccia_step_2", duration: 3 },
      { text: "recipe_gf_focaccia_step_3", duration: 7 },
      { text: "recipe_gf_focaccia_step_4", duration: 30 },
      { text: "recipe_gf_focaccia_step_5", duration: 60 },
      { text: "recipe_gf_focaccia_step_6", duration: 30 },
      { text: "recipe_gf_focaccia_step_7", duration: 15 }
    ]
  },
  { 
    id: 'gf_pan_pizza', 
    category: 'pizza',
    nameKey: 'recipe_gf_pan_pizza', 
    hours: 4, 
    defaultTemp: 285,
    hydration: 0.85,
    flour: 'Caputo Gluten Free Flour',
    image: 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=600&q=80',
    ingredients: [
      "1kg Caputo Gluten Free Flour",
      "850g Water",
      "15g Yeast",
      "25g Salt",
      "30g Olive Oil",
      "Toppings: Tomato Sauce, Cheese"
    ],
    ingredients_he: [
      "1 ק״ג קמח קאפוטו ללא גלוטן",
      "850 גרם מים",
      "15 גרם שמרים",
      "25 גרם מלח",
      "30 גרם שמן זית",
      "תוספות: רוטב עגבניות, גבינה"
    ],
    steps: [
      { text: "recipe_gf_pan_step_1", duration: 10 },
      { text: "recipe_gf_pan_step_2", duration: 30 },
      { text: "recipe_gf_pan_step_3", duration: 120 },
      { text: "recipe_gf_pan_step_4", duration: 8 },
      { text: "recipe_gf_pan_step_5", duration: 6 }
    ]
  },
  { 
    id: 'sourdough', 
    category: 'pizza',
    nameKey: 'recipe_sourdough', 
    hours: 24, 
    defaultTemp: 285,
    hydration: 0.64,
    flour: 'Caputo "00" Chef\'s Flour',
    image: 'https://images.unsplash.com/photo-1585238342024-78d387f4a707?auto=format&fit=crop&w=600&q=80',
    ingredients: [
      "1kg Caputo \"00\" Chef's Flour",
      "640g Water",
      "200g Sourdough Starter",
      "25g Salt",
      "Toppings: Tomato Sauce, Mozzarella"
    ],
    ingredients_he: [
      "1 ק״ג קמח קאפוטו שף 00",
      "640 גרם מים",
      "200 גרם מחמצת",
      "25 גרם מלח",
      "תוספות: רוטב עגבניות, מוצרלה"
    ],
    steps: [
      { text: "recipe_sourdough_step_1", duration: 10 },
      { text: "recipe_sourdough_step_2", duration: 60 },
      { text: "recipe_sourdough_step_3", duration: 360 },
      { text: "recipe_sourdough_step_4", duration: 180 },
      { text: "recipe_sourdough_step_5", duration: 40 },
      { text: "recipe_sourdough_step_6", duration: 11 }
    ]
  },
  { 
    id: 'quick_4h', 
    category: 'pizza',
    nameKey: 'recipe_quick_4h', 
    hours: 4, 
    defaultTemp: 285,
    hydration: 0.65,
    flour: 'Caputo "00" Pizzeria Flour',
    image: 'https://images.unsplash.com/photo-1593560708920-61dd98c46a4e?auto=format&fit=crop&w=600&q=80',
    ingredients: [
      "1kg Caputo \"00\" Pizzeria Flour",
      "650g Water",
      "15g Yeast",
      "25g Salt",
      "20g Olive Oil",
      "Toppings: Tomato Sauce, Cheese"
    ],
    ingredients_he: [
      "1 ק״ג קמח קאפוטו פיצריה 00",
      "650 גרם מים",
      "15 גרם שמרים",
      "25 גרם מלח",
      "20 גרם שמן זית",
      "תוספות: רוטב עגבניות, גבינה"
    ],
    steps: [
      { text: "recipe_quick_4h_step_1", duration: 5 },
      { text: "recipe_quick_4h_step_2", duration: 30 },
      { text: "recipe_quick_4h_step_3", duration: 30 },
      { text: "recipe_quick_4h_step_4", duration: 180 },
      { text: "recipe_quick_4h_step_5", duration: 40 },
      { text: "recipe_quick_4h_step_6", duration: 7 }
    ]
  }
];
