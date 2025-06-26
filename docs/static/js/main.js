// Initialize Lucide Icons
lucide.createIcons();

// Copy to clipboard functionality
function copyToClipboard(button) {
    const textToCopy = document.getElementById('citation-text').innerText;
    const textarea = document.createElement('textarea');
    textarea.value = textToCopy;
    document.body.appendChild(textarea);
    textarea.select();
    try {
        document.execCommand('copy');
        // Change icon to feedback
        button.innerHTML = '<i data-lucide="check" class="w-4 h-4 text-green-400"></i>';
        lucide.createIcons();
        setTimeout(() => {
            button.innerHTML = '<i data-lucide="copy" class="w-4 h-4"></i>';
            lucide.createIcons();
        }, 2000);
    } catch (err) {
        console.error('Failed to copy text: ', err);
        alert('コピーに失敗しました。');
    }
    document.body.removeChild(textarea);
}

// Theme toggle functionality
const themeToggleButton = document.getElementById('theme-toggle');
const sunIcon = document.getElementById('theme-toggle-sun');
const moonIcon = document.getElementById('theme-toggle-moon');

const getCurrentTheme = () => document.documentElement.classList.contains('dark') ? 'dark' : 'light';

const applyTheme = (theme) => {
    if (theme === 'dark') {
        document.documentElement.classList.add('dark');
        sunIcon.classList.add('hidden');
        moonIcon.classList.remove('hidden');
    } else {
        document.documentElement.classList.remove('dark');
        sunIcon.classList.remove('hidden');
        moonIcon.classList.add('hidden');
    }
};

const savedTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
applyTheme(savedTheme);

themeToggleButton.addEventListener('click', () => {
    const newTheme = getCurrentTheme() === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', newTheme);
    applyTheme(newTheme);
});

// Tab toggle functionality
const tabsContainer = document.querySelector('#tasks');
if (tabsContainer) {
    const desktopTabs = tabsContainer.querySelector('#desktop-tabs');
    const tabButtons = desktopTabs.querySelectorAll('[role="tab"]');
    const tabPanels = tabsContainer.querySelectorAll('[role="tabpanel"]');
    const mobileDropdownTrigger = tabsContainer.querySelector('#mobile-tabs-trigger');
    const mobileDropdownLabel = tabsContainer.querySelector('#mobile-tabs-label');
    const mobileDropdownMenu = tabsContainer.querySelector('#mobile-tabs-menu');
    const mobileDropdownItems = tabsContainer.querySelectorAll('.dropdown-item');

    const showTab = (panelId) => {
        tabPanels.forEach(panel => {
            panel.classList.toggle('hidden', panel.id !== panelId);
        });
    };

    const setActive = (panelId) => {
        const selectedText = document.querySelector(`.dropdown-item[data-panel="${panelId}"]`).textContent;

        // Update desktop tabs
        tabButtons.forEach(btn => {
            const isSelected = btn.getAttribute('aria-controls') === panelId;
            btn.classList.toggle('active-tab', isSelected);
            btn.setAttribute('aria-selected', isSelected);
        });

        // Update mobile dropdown label
        if (mobileDropdownLabel) mobileDropdownLabel.textContent = selectedText;

        showTab(panelId);
    };

    tabButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const panelId = button.getAttribute('aria-controls');
            setActive(panelId);
        });
    });

    if (mobileDropdownTrigger) {
        mobileDropdownTrigger.addEventListener('click', () => {
            mobileDropdownMenu.classList.toggle('hidden');
        });
    }

    mobileDropdownItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const panelId = item.getAttribute('data-panel');
            setActive(panelId);
            if(mobileDropdownMenu) mobileDropdownMenu.classList.add('hidden');
        });
    });

    window.addEventListener('click', (e) => {
        if (mobileDropdownTrigger && !mobileDropdownTrigger.contains(e.target) && mobileDropdownMenu && !mobileDropdownMenu.contains(e.target)) {
            mobileDropdownMenu.classList.add('hidden');
        }
    });
}


// Accordion functionality
const accordionTriggers = document.querySelectorAll('.accordion-trigger');
accordionTriggers.forEach(trigger => {
    trigger.addEventListener('click', () => {
        const content = trigger.nextElementSibling;
        const isExpanded = trigger.getAttribute('aria-expanded') === 'true';

        trigger.setAttribute('aria-expanded', !isExpanded);
        if (!isExpanded) {
            content.style.maxHeight = content.scrollHeight + 'px';
        } else {
            content.style.maxHeight = '0';
        }
    });
});

// Embla Carousel functionality
const setupEmblaCarousel = (emblaNode) => {
    if (!emblaNode) return;
    const viewportNode = emblaNode.querySelector('.embla__viewport');
    const prevBtnNode = emblaNode.querySelector('.embla__button--prev');
    const nextBtnNode = emblaNode.querySelector('.embla__button--next');
    const dotsNode = emblaNode.querySelector('.embla__dots');

    if (!viewportNode) return;

    const emblaApi = EmblaCarousel(viewportNode, { align: 'center', loop: true });

    const TWEEN_FACTOR_BASE = 0.2
    let tweenFactor = 0
    let tweenNodes = []

    const setTweenNodes = (emblaApi) => {
        tweenNodes = emblaApi.slideNodes().map((slideNode) => {
            return slideNode.querySelector('.embla__parallax__layer');
        })
    }

    const setTweenFactor = (emblaApi) => {
        tweenFactor = TWEEN_FACTOR_BASE * emblaApi.scrollSnapList().length
    }

    const tweenParallax = (emblaApi, eventName) => {
        const engine = emblaApi.internalEngine();
        const scrollProgress = emblaApi.scrollProgress();
        const slidesInView = emblaApi.slidesInView();
        const isScrollEvent = eventName === 'scroll';

        emblaApi.scrollSnapList().forEach((scrollSnap, snapIndex) => {
            let diffToTarget = scrollSnap - scrollProgress;
            const slidesInSnap = engine.slideRegistry[snapIndex];

            slidesInSnap.forEach((slideIndex) => {
            if (isScrollEvent && !slidesInView.includes(slideIndex)) return;

            if (engine.options.loop) {
                engine.slideLooper.loopPoints.forEach((loopItem) => {
                const target = loopItem.target();
                if (slideIndex === loopItem.index && target !== 0) {
                    const sign = Math.sign(target);
                    if (sign === -1) diffToTarget = scrollSnap - (1 + scrollProgress);
                    if (sign === 1) diffToTarget = scrollSnap + (1 - scrollProgress);
                }
                })
            }
            const translate = diffToTarget * (-1 * tweenFactor) * 100;
            const tweenNode = tweenNodes[slideIndex];
            if (tweenNode) tweenNode.style.transform = `translateX(${translate}%)`;
            });
        });
    };

    const addDotBtnsAndClickHandlers = (emblaApi, dotsNode) => {
        let dotNodes = []
        if (dotsNode) {
            dotsNode.innerHTML = emblaApi.scrollSnapList().map(() => '<button class="embla__dot" type="button"></button>').join('')
            dotNodes = Array.from(dotsNode.querySelectorAll('.embla__dot'))
            dotNodes.forEach((dotNode, index) => {
                dotNode.addEventListener('click', () => emblaApi.scrollTo(index), false)
            })
        }
        return dotNodes
    }

    const toggleDotBtnsActive = (emblaApi, dotNodes) => {
        const selected = emblaApi.selectedScrollSnap()
        dotNodes.forEach((dotNode, index) => {
            dotNode.classList.toggle('embla__dot--selected', index === selected)
        })
    }

    const dotNodes = addDotBtnsAndClickHandlers(emblaApi, dotsNode);

    const onSelect = (emblaApi) => {
        toggleDotBtnsActive(emblaApi, dotNodes);
        if(prevBtnNode) prevBtnNode.disabled = !emblaApi.canScrollPrev();
        if(nextBtnNode) nextBtnNode.disabled = !emblaApi.canScrollNext();
    }

    if(prevBtnNode) prevBtnNode.addEventListener('click', emblaApi.scrollPrev, false);
    if(nextBtnNode) nextBtnNode.addEventListener('click', emblaApi.scrollNext, false);

    emblaApi.on('select', onSelect);
    emblaApi.on('reInit', onSelect);
    emblaApi.on('reInit', setTweenNodes);
    emblaApi.on('reInit', setTweenFactor);
    emblaApi.on('reInit', tweenParallax);
    emblaApi.on('scroll', tweenParallax);

    setTweenNodes(emblaApi);
    setTweenFactor(emblaApi);
    tweenParallax(emblaApi);
    onSelect(emblaApi);
};

const overviewCarouselNode = document.querySelector('#overview-carousel');
if (overviewCarouselNode) {
    setupEmblaCarousel(overviewCarouselNode);
}
